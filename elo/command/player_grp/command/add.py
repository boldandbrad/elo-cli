"""Player Add Sub Command"""

import click

from elo.util.db_util import db_init, db_connect, db_close
from elo.util.config_util import get_config_value

from elo.service.player_service import get_or_create_by_name


@click.command(help="Add a player to the active series.")
@click.help_option("-h", "--help")
@click.argument("name", type=str, required=True)
def add_player(name: str):
    """Add a player to the active series.

    Args:
        name (str): player name
    """
    # TODO: check if series already exists
    active_series = get_config_value("active-series")
    active_db = db_init(active_series)

    db_connect(active_db)

    _ = get_or_create_by_name(name)

    db_close(active_db)
