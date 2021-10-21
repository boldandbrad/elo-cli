
import click
from loguru import logger

from elocli.command.series_cmds.add import add_series
from elocli.command.series_cmds.list import list_series
from elocli.command.series_cmds.set import set_series


@click.group(
    help='Manage results series.'
)
@click.help_option(
    '-h', '--help'
)
def series():
    pass


series.add_command(add_series, 'add')
series.add_command(list_series, 'list')
series.add_command(set_series, 'set')
