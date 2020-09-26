#!/usr/bin/env python3
'''CLI DEIFINITION'''
import click


LABEL_SIZES = ['60']

PRINTER_HELPER = "The identifier for the printer. This could be a string like tcp://192.168.1.21:9100 for a networked printer or usb://0x04f9:0x2015/000M6Z401370 for a printer connected via USB."
@click.group()
@click.option('-b', '--backend', default='linux_kernel', metavar='BACKEND_IDENTIFIER', envvar='BROTHER_QL_BACKEND', help='Not implemented!')
@click.option('-m', '--model', default='Gc420t', metavar='MODEL_IDENTIFIER', envvar='BROTHER_QL_MODEL', help='Not implemented!')
@click.option('-p', '--printer', metavar='PRINTER_IDENTIFIER', envvar='ZEBRA_PRINTER', help=PRINTER_HELPER)
@click.option('--debug', is_flag=True)
@click.version_option()
@click.pass_context
def cli(ctx, *args, **kwargs):
    """ Command line interface for the suflex_zebra Python package. """
    backend = kwargs.get('backend', None)
    model = kwargs.get('model', None)
    printer = kwargs.get('printer', None)
    debug = kwargs.get('debug')

    ctx.meta['MODEL'] = model
    ctx.meta['BACKEND'] = backend
    ctx.meta['PRINTER'] = printer

@cli.command()
@click.pass_context
def discover(ctx):
    """ find connected label printers """
    discover_and_list_available_devices()

def discover_and_list_available_devices():
    from suflex_zebra.linux_kernel import list_available_devices
    from suflex_zebra.output_helpers import log_discovered_devices, textual_description_discovered_devices
    available_devices = list_available_devices()
    log_discovered_devices(available_devices)
    print(textual_description_discovered_devices(available_devices))




@cli.command('print', short_help='Print a label')
@click.argument('images', nargs=-1, type=click.File('rb'), metavar='IMAGE [IMAGE] ...')
@click.option('-l', '--label', default=60, envvar='ZEBRA_LABEL', help='Not implemented!')
@click.pass_context
def print_cmd(ctx, *args, **kwargs):
    """ Print a label of the provided IMAGE. """
    from suflex_zebra.zebra_interface import create_zpl, send_print
    printer = ctx.meta.get('PRINTER')
    payload = create_zpl(kwargs['images'])
    send_print(printer, payload)
