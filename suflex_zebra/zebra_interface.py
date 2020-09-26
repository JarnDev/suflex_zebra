#!/usr/bin/env python
import zpl
from PIL import Image

RIBBON_WIDTH = 98
LABEL_WIDTH = 60
LABEL_HEIGTH = 60
PRINTER_DPMM = 8
PRINT_OFFSET = 19

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
            device_specifier = device_specifier[6:]

    for zpl_payload in payload:
        with open('/dev/usb/lp0', 'w') as printer:
            printer.write(zpl_payload)
