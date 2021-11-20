"""Series List Sub Command"""

import click

from elo.util.db_util import get_dbs
from elo.util.config_util import get_config_value


@click.command(help="List all created series.")
@click.help_option("-h", "--help")
def list_series():
    """List all created series."""
    active_series = get_config_value("active-series")

    series_list = get_dbs()
    for series in series_list:
        if series == active_series:
            print(f"{series} (active)")
        else:
            print(series)