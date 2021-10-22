"""Match List Sub Command"""

import click

from elocli.util.db_util import db_init, db_connect, db_close
from elocli.util.config_util import get_config_value

from elocli.service import match_service, player_service


@click.command(help="List all matches in the active series.")
@click.help_option("-h", "--help")
def list_matches():
    """List all matches in the active series."""
    # TODO: check if series already exists
    active_series = get_config_value("active-series")
    active_db = db_init(active_series)

    db_connect(active_db)

    matches = match_service.get_all_ordered()
    for match in matches:
        home_player = player_service.get_by_id(match.home_id)
        away_player = player_service.get_by_id(match.away_id)
        if match.sudden_death:
            print(
                f"{home_player.name} {match.home_score}\t{match.away_score} {away_player.name} SD"
            )
        else:
            print(
                f"{home_player.name} {match.home_score}\t{match.away_score} {away_player.name}"
            )

    db_close(active_db)
