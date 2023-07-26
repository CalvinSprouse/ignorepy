#!/usr/bin/env python

"""
Accesses 'https://www.toptal.com/developers/gitignore/api/'
to generate a gitignore and copies to the clipboard.
"""

# imports
import sys
import requests

# attempt to import pyperclip and recommend install if it fails
try:
    import pyperclip
except ImportError:
    print("Could not find module 'pyperclip'. Please install and run again.")

# attempt to import rich, but its not required
try:
    from rich import print
except ImportError:
    pass


# define a base-link to the gitignore generator
web_base = "https://www.toptal.com/developers/gitignore/api/"

# load arguments to generate the api
ignore_args = ["python", "macos", "visualstudiocode", "windows", "venv"]
ignore_arg_str = ",".join(ignore_args)

# define the full api access link
link = web_base + ignore_arg_str
# print(f"Generating .gitignore w/args: {', '.join(ignore_args)}.")

# get the web text using a request session
session = requests.Session()
response = session.get(link, headers={'User-Agent': 'Mozilla/5.0'})

# get the response code and ensure it is good
# if not print a warning message
response_code = response.status_code
if response_code != 200:
    print(f"Error: response code {response_code}.")
    sys.exit(code=1)

# get the raw text from the response
raw_text = str(response.content.decode())

# copy the text to the clipboard
pyperclip.copy(raw_text)

# print that the terminal is done
# print how many lines were copied
line_count = len(raw_text.split('\n'))
# print(f"{line_count} .gitignore lines copied.")
print(f"Generated {line_count} .gitignore lines w/args: '{', '.join(ignore_args)}'.")
