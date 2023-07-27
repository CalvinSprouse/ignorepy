# ignorepy
Generate a .gitignore from the command line.

## Installation
Install with pip:

``` bash
pip install ignorepy
```

## Usage
After installing run:

``` bash
ignorepy tag1 tag2 tag3
```

A .gitignore file will be generated from [gitignore.io](https://www.toptal.com/developers/gitignore) with the specified tags and copied to the clipboard.

Additionally pass -s
``` bash
ignorepy tag1 tag2 tag3 -s
```

and the tags will be saved as default tag.
Then the program can be called with
``` bash
ignorepy
```
and the default tags will be automatically loaded.

Additionally pass -f
``` bash
ignorepy tag1 tag2 tag3 -f
```
and instead of being copied to the clipboard the .gitignore file will be written to .gitignore in the current working directory.
