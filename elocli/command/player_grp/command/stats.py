"""Player Stats Sub Command"""

import click

from elocli.util.db_util import db_init, db_connect, db_close
from elocli.util.config_util import get_config_value

from elocli.service.player_service import get_by_name


@click.command(help="Print a player's stats from the active series.")
@click.help_option("-h", "--help")
@click.argument("name", required=True)
def stats_player(name: str):
    """Print a player's stats from the active series.

    Args:
        name (str): player name
    """
    # TODO: check if series already exists
    active_series = get_config_value("active-series")
    active_db = db_init(active_series)

    db_connect(active_db)

    player = get_by_name(name)
    matches_played = player.wins + player.losses + player.draws
    point_diff = player.points_for - player.points_against

    print(player.name)
    print("----------------")
    print(f"Elo:\t{player.elo}")
    print(f"W:\t{player.wins}")
    print(f"L:\t{player.losses}")
    print(f"D:\t{player.draws}")
    print(f"M:\t{matches_played}")
    print(f"PF:\t{player.points_for}")
    print(f"PA:\t{player.points_against}")
    print(f"PD:\t{point_diff}")

    db_close(active_db)
