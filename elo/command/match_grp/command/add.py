"""Match Add Sub Command"""

from typing import Tuple

import click

from elo.util.db_util import db_init, db_connect, db_close
from elo.util.config_util import get_config_value
from elo.util.rating_util import update_elos, update_stats

from elo.model.match import Match

from elo.service import player_service


@click.command(help="Add a match to the active series.")
@click.help_option("-h", "--help")
@click.argument("home", nargs=2)
@click.argument(
    "away",
    nargs=2,
)
@click.option("-s", "--sd", is_flag=True, required=False)
def add_match(home: Tuple[str, int], away: Tuple[str, int], sd: bool):
    """Add a match to the active series.

    Args:
        home (Tuple[str, int]): name and score of home player
        away (Tuple[str, int]): name and score of away player
        sd (bool): sudden death
    """
    # TODO: check if series already exists
    active_series = get_config_value("active-series")
    active_db = db_init(active_series)

    db_connect(active_db)

    # TODO: check for invalid args

    # TODO: check if players do not yet exist
    home_player = player_service.get_by_name(home[0])
    away_player = player_service.get_by_name(away[0])

    # grab scores from args
    home_score = int(home[1])
    away_score = int(away[1])

    # calculate updated player elos based on match outcome
    home_player.elo, away_player.elo, rating_change = update_elos(
        home_player.elo, away_player.elo, home_score, away_score
    )

    # update player stats based on outcome
    update_stats(home_player, away_player, home_score, away_score)

    home_player.save()
    away_player.save()

    match = Match(
        home_id=home_player.id,
        away_id=away_player.id,
        home_score=home_score,
        away_score=away_score,
        sudden_death=sd,
        rating_change=rating_change,
    )

    match.save()
    print("match recorded")

    db_close(active_db)
