#!/usr/bin/env python

"""
Accesses 'https://www.toptal.com/developers/gitignore/api/'
to generate a gitignore and copies to the clipboard.
"""

# imports
import argparse
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


# define a function to generate the gitignore from the gitignore webpage
def generate_gitignore(ignore_tags: list[str]) -> str:
    """Generates a .gitignore file from the gitignore.io api.

    Arguments:
        ignore_tags -- list of strings to use as tags for the gitignore.

    Returns:
        raw_text -- the raw text from the api call.
    """

    # define the base link to the webpage
    web_base = "https://www.toptal.com/developers/gitignore/api/"

    # load the arguments to generate the api call
    ignore_tags = [t.lower().strip() for t in ignore_tags]
    ignore_str = ",".join(ignore_tags)

    # generate the link
    link = web_base + ignore_str

    # get the web text using a request session
    session = requests.Session()
    response = session.get(link, headers={"User-Agent": "Mozilla/5.0"})

    # get the response code
    response_code = response.status_code

    # get the raw text from the response
    raw_text = str(response.content.decode())

    # return the raw text
    return raw_text, response_code


# run the main script
if __name__ == "__main__":
    # get tags from the user using argparse
    # user can pass an unlimited number of tags to the program
    # add an optional tag, -s which saves the arguments as the default
    # then if no arguments are called the defauls are used
    parser = argparse.ArgumentParser(
        description="Generate a gitignore from gitignore.io."
    )

    # add the arguments to the parser
    parser.add_argument(
        "-s", "--save", action="store_true",
        help="save the tags as the defaults for future use.",
    )

    # add the tags to the parser
    parser.add_argument(
        "tags", nargs="*",
        help="tags to use for the gitignore.",
    )

    # parse the arguments
    args = parser.parse_args()


    # define the location of the defaults file
    defaults_file = ".defaults"

    # check if -s was passed, if so save the tags to the defaults file
    # otherwise check if any tags were passed, if not load from defaults if it exists
    if args.save:
        # ensure a tag was passed to -s (cant call -s alone)
        if len(args.tags) == 0:
            print("Error: no tags passed with -s.")
            sys.exit(1)

        # open the defaults file and write the tags to it
        with open(defaults_file, "w", encoding="utf-8") as f:
            f.write("\n".join(args.tags))

        # print that the defaults were saved
        print(f"Saved {args.tags} tags as the defaults.")
    elif len(args.tags) == 0:
        # open the defaults file and load the tags from it
        try:
            with open(defaults_file, "r", encoding="utf-8") as f:
                args.tags = f.read().split("\n")

            print(f"Loaded {args.tags} from defaults.")
        except FileNotFoundError:
            print("Error: no tags passed and no defaults file found.")
            print("Use -s to save a list of tags as defaults.")
            sys.exit(1)


    # generate the ignore text from the function
    ignore_response = generate_gitignore(ignore_tags=args.tags)

    # check the response code
    if ignore_response[1] != 200:
        print("Error: could not generate gitignore. Website response:")
        print(ignore_response[0].strip())
        sys.exit(1)

    # copy the text to the clipboard
    pyperclip.copy(ignore_response[0])

    # print that the program is done
    line_count = len(ignore_response[0].split('\n'))
    print(f"Copied {line_count} lines to the clipboard.")
