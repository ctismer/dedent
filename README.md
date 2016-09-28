# dedent
The simple detent module, which makes writing inline code easy.

## Usage:

  python -c dedent.py "\<some code>"
    
or

  python -m dedent "\<some code>"
 
Dedent the next program on the command line and execute it.

This has the nice effect that the inline code can be freely indented.

The script replaces the "-c" parameter.
Alternatively, you can also use "-m" without ".py".

There is no shebang line by intent. It is not meant as a standalone script.

Inspired by a comment from Frederik Gladhorn.
