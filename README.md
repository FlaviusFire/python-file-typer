# python-file-typer
Copy contents of a file in clip-board limited scenarios via keyboard input

This script will take the text from a file and auto-type it via keyboard input. The intended use is to copy text or code to an environment where the clipboard is not available, such as in a browser-based VM in a CTF competition.

Known issues:
Indendation is currently inconsistantly functional. Assume it won't properly duplicate indentation or "tabs".
Sometimes typing will appear to freeze, which I imagine is Windows struggling to handle all the input commands. Moving the curser usually solves the issue.
