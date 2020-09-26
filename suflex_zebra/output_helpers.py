#!/usr/bin/env python
import platform


def log_on_linux(msg):
    if platform.system() == 'Linux':
        from syslog import syslog, LOG_INFO
        print("TESTE SYSLOG")
        syslog(LOG_INFO, msg)


def log_discovered_devices(available_devices):
    for device in available_devices:
        result = {'model': 'unknown'}
        result.update(device)
        log_on_linux("Found a label printer: {identifier}  (model: {model})".format(**result))


def textual_description_discovered_devices(available_devices):
    output = ""
    for device in available_devices:
        output += device['identifier']
    return output

