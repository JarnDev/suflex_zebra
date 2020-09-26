#!/usr/bin/env python
import logging

LOGGER = logging.getLogger(__name__)
SYSLOG_HANDLER = logging.handlers.SysLogHandler(address='/dev/log')
LOGGER.addHandler(SYSLOG_HANDLER)


def log_discovered_devices(available_devices, level=logging.INFO):
    for device in available_devices:
        result = {'model': 'unknown'}
        result.update(device)
        LOGGER.log(level, "Found a label printer: {identifier}  (model: {model})".format(**result))

def textual_description_discovered_devices(available_devices):
    output = ""
    for device in available_devices:
        output += device['identifier']
    return output
