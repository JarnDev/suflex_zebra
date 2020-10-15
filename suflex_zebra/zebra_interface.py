#!/usr/bin/env python
import sys
import os
import zpl
from PIL import Image
from suflex_zebra.output_helpers import log_on_linux
LABEL_WIDTH = int(os.environ.get("LABEL_WIDTH", 60))
LABEL_HEIGTH = int(os.environ.get("LABEL_HEIGTH", 60))
PRINTER_DPMM = int(os.environ.get("PRINTER_DPMM", 8))
PRINT_OFFSET = int(os.environ.get("PRINT_OFFSET", 22))

def create_zpl(images):
    '''Create ZPL from Image'''
    payload_zpl = []
    for image in images:
        if isinstance(image, Image.Image):
            loaded_image = image
        else:
            try:
                loaded_image = Image.open(image)
            except:
                raise NotImplementedError("The image argument needs to be an Image() instance, the filename to an image, or a file handle.")

        label = zpl.Label(LABEL_HEIGTH, LABEL_WIDTH, PRINTER_DPMM)
        label.set_darkness(30)
        label.origin(PRINT_OFFSET, 0)
        label.write_graphic(loaded_image, LABEL_WIDTH, LABEL_HEIGTH)
        label.endorigin()
        payload_zpl.append(label.dumpZPL())
    return payload_zpl

def send_print(device_specifier, payload):
    '''Send zpl code to zebra'''
    if isinstance(device_specifier, str):
        if device_specifier.startswith('file://'):
            device_specifier = device_specifier[7:]
    try:
        for zpl_payload in payload:
            with open(device_specifier, 'w') as printer:
                printer.write(zpl_payload)
        print('Job successfully printed')
        log_on_linux('Job successfully printed')
        sys.exit(0)
    except Exception as error:
        log_on_linux(f'Error: an error occurred while printing: {error}')
        print(f'Error: an error occurred while printing: {error}')
        sys.exit(2)
