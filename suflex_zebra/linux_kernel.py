#!/usr/bin/env python
import glob

def list_available_devices():
    """
    List all available devices for the linux kernel backend
    returns: devices: a list of dictionaries with the keys 'identifier' and 'instance': \
        [ {'identifier': 'file:///dev/usb/lp0', 'instance': None}, ] \
        Instance is set to None because we don't want to open (and thus potentially block) the device here.
    """

    paths = glob.glob('/dev/usb/lp*')

    return [{'identifier': 'file://' + path, 'instance': None} for path in paths]