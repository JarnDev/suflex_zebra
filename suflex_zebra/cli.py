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
@click.option('-r', '--rotate', type=click.Choice(('auto', '0', '90', '180', '270')), default='auto', help='Rotate the image (counterclock-wise) by this amount of degrees.')
@click.option('-t', '--threshold', type=float, default=70.0, help='The threshold value (in percent) to discriminate between black and white pixels.')
@click.option('-d', '--dither', is_flag=True, help='Enable dithering when converting the image to b/w. If set, --threshold is meaningless.')
@click.option('-c', '--compress', is_flag=True, help='Enable compression (if available with the model). Label creation can take slightly longer but the resulting instruction size is normally considerably smaller.')
@click.option('--red', is_flag=True, help='Create a label to be printed on black/red/white tape (only with QL-8xx series on DK-22251 labels). You must use this option when printing on black/red tape, even when not printing red.')
@click.option('--600dpi', 'dpi_600', is_flag=True, help='Print with 600x300 dpi available on some models. Provide your image as 600x600 dpi; perpendicular to the feeding the image will be resized to 300dpi.')
@click.option('--lq', is_flag=True, help='Print with low quality (faster). Default is high quality.')
@click.option('--no-cut', is_flag=True, help="Don't cut the tape after printing the label.")
@click.option('--rasp', is_flag=True, help="Use raspberry printer method")
@click.pass_context
def print_cmd(ctx, *args, **kwargs):
    """ Print a label of the provided IMAGE. """
    from suflex_zebra.output_helpers import log_on_linux
    from suflex_zebra.zebra_interface import create_zpl, send_print


    printer = ctx.meta.get('PRINTER')
    payload = create_zpl(kwargs['images'])
    send_print(printer, payload)
    log_on_linux(f"printer:{printer} | imagens: {kwargs['images']}")
