"""Elo Series Sub Command"""

import click

# from loguru import logger

from .command.add import add_series
from .command.list import list_series
from .command.set import set_series


@click.group(help="Manage results series.")
@click.help_option("-h", "--help")
def series():
    """Manage results series."""


series.add_command(add_series, "add")
series.add_command(list_series, "list")
series.add_command(set_series, "set")
