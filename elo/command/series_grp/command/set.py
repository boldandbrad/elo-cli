"""Series Set Sub Command"""

import click

from elo.util.db_util import get_dbs

from elo.util.config_util import set_config_value

# from elo.model.base import db


@click.command(help="Set an existing series to active.")
@click.help_option("-h", "--help")
@click.argument("name", required=True)
def set_series(name: str):
    """Set an existing series to active.

    Args:
        name (str): series name
    """
    # TODO: check if series exists before setting

    series_list = get_dbs()
    if name in series_list:
        set_config_value("active-series", name)
        print("set active series: " + name)
    else:
        print(f"Series '{name}' does not exist. Could not set as active.")
