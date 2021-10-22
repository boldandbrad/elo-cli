"""Player List Sub Command"""

import click

from elocli.util.db_util import db_init, db_connect, db_close
from elocli.util.config_util import get_config_value

from elocli.service.player_service import get_all_ordered


@click.command(help="List all players in the active series.")
@click.help_option("-h", "--help")
def list_players():
    """List all players in the active series."""
    # TODO: check if series already exists
    active_series = get_config_value("active-series")
    active_db = db_init(active_series)

    db_connect(active_db)

    players = get_all_ordered()
    for player in players:
        print(player.name)

    db_close(active_db)
