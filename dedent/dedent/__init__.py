from __future__ import print_function

"""
Dedent the next program on the command line and execute it.

This has the nice effect that the inline code can be freely indented.

The script replaces the "-c" parameter.
Alternatively, you can also use "-m" without ".py".

There is no shebang line by intent. It is not meant as a standalone script.

Inspired by a comment from Frederik Gladhorn.
"""

import sys
import os
import traceback
import textwrap
import argparse
import __future__

default_flags = (__future__.CO_FUTURE_DIVISION +
                 __future__.CO_FUTURE_ABSOLUTE_IMPORT +
                 __future__.CO_FUTURE_PRINT_FUNCTION +
                 __future__.CO_FUTURE_UNICODE_LITERALS)

PY3 = sys.version_info[0] >= 3


def variant_parser(init):
    description = 'Indent Your Program. We dedent it.'
    if PY3:
        parser = argparse.ArgumentParser(description=description, allow_abbrev=False)
    else:
        parser = argparse.ArgumentParser(description=description) # :-(
    parser.add_argument('--future', '-f', action='store_true', help=
        'you can switch all __future__ statements on with the --future flag.')
    if init:
        parser.add_argument('__init__', nargs=1,
                            help='this is just the name of this module.')
    parser.add_argument('program', nargs="+", help=
                        'Your program text to be dedented.')

    args = parser.parse_args()
    return args

# if someone calls "__init__" directly, we need to handle an extra argument.
args = variant_parser(False)
if args.program[0] == "__init__":
    args = variant_parser(True)

prog = args.program[0]

text = textwrap.dedent(prog + "\n")
flags = default_flags if args.future else 0
__name__ = "__main__"

try:
    exec(compile(text, "<string>", "exec", flags, True))
except:
    # we want to format the exception as if no frame was on top.
    exp, val, tb = sys.exc_info()
    listing = traceback.format_exception(exp, val, tb)
    # remove the entry for the first frame
    del listing[1]
    files = [line for line in listing if line.startswith("  File")]
    if len(files) == 1:
        # only one file, remove the header.
        del listing[0]
    print("".join(listing), file=sys.stderr)
    sys.exit(1)
