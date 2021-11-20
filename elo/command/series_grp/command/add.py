"""Series Add Sub Command"""

import click

from elo.util.db_util import db_init
from elo.util.config_util import set_config_value


@click.command(help="Add and activate a new series.")
@click.help_option("-h", "--help")
@click.argument("name", required=True)
def add_series(name: str):
    """Add and activate a new series.

    Args:
        name (str): series name
    """
    # TODO: check if series already exists
    _ = db_init(name)
    set_config_value("active-series", name)
    print("added series " + name)
