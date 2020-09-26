# SUFLEX ZEBRA

#A python package created for Zebra integration with suflex software.

## Installation


Install the latest version from Github using:

    pip install --upgrade https://github.com/jarndev/brother_ql/archive/master.zip

This package was mainly created for use with Python 3.
The essential functionality, however, will also work with Python 2: the creation of label files.

In order to run the `suflex_zebra` command line utility, the directory it resides in
needs to be in the PATH envirnoment variable.
On some systems, the `pip install` command defaults to the `--user` flag resulting in the utility
being put in the `~/.local/bin` directory.
On those systems, extending the path variable via `export PATH="${PATH}:~/.local/bin"` is needed.

## Usage

The main user interface of this package is the command line tool `suflex_zebra`.

    Usage: suflex_zebra [OPTIONS] COMMAND [ARGS]...
    
        Command line interface for the suflex_zebra Python package.
    
    Options:
      -b, --backend BACKEND_IDENTIFIER **Not implemented!
      -m, --model MODEL_IDENTIFIER **Not implemented!
      -p, --printer PRINTER_IDENTIFIER
                                      The identifier for the printer. This could
                                      be a string like tcp://192.168.1.21:9100 for
                                      a networked printer or
                                      usb://0x04f9:0x2015/000M6Z401370 for a
                                      printer connected via USB.
      --debug
      --version                       Show the version and exit.
      --help                          Show this message and exit.
    
    Commands:
      discover  find connected label printers
      print     Print a label

The most important command is the `print` command and here is its CLI signature:

    Usage: suflex_zebra print [OPTIONS] IMAGE [IMAGE] ...
    
      Print a label of the provided IMAGE.
    
    Options:
      -l, --label LABEL_IDENTIFIER **Not implemented!

So, printing images file can be as easy as:

    suflex_zebra -p /deb/usb/lp* print my_image1.png my_image2.png ...



This package was derived from https://github.com/pklaus/brother_ql/ created for brother label printers used at the company, I just built a package that accepts the most used commands for minimal code changes at company code sources.