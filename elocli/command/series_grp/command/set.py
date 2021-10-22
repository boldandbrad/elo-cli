"""Series Set Sub Command"""

import click

# from elocli.util.db_util import db_init
from elocli.util.config_util import set_config_value

# from elocli.model.base import db


@click.command(help="Set an existing series to active.")
@click.help_option("-h", "--help")
@click.argument("name", required=True)
def set_series(name: str):
    """Set an existing series to active.

    Args:
        name (str): series name
    """
    # TODO: check if series exists before setting
    set_config_value("active-series", name)
    print("set active series: " + name)
