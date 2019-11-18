# Parsing Table of Contents

## Intent and Overview
This was an exercise to parse the XML formmated toc.ncx file exported from a *.epub file and generate a simple text file. The 'toc.ncx' file was extracted from the *.epub file using calibre. This was written as a practice for creating an executable python app to run on Ubuntu 18.04 using Python 3.7.3.

## Additional Notes
1. ensure that you have the #! /path/to/python at the top of the file
	* you can find this using ```which python``` from the bash terminal

2. to make the file accessible globally, copy the file to /usr/local/bin

```{bash}
chmod +x parse_toc.py
sudo cp parse_toc.py /usr/local/bin/parse_toc
```

3. Test if everything is functional

```{bash}
parse_toc toc.ncx
```

It should print...

> Now running /usr/local/bin/parse_toc script on file toc.ncx...
> Success.

...and a file called "toc_output.txt" should appear.


