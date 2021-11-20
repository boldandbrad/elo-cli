"""Match Add Sub Command"""

from typing import Tuple

import click

from elo.util.db_util import db_init, db_connect, db_close
from elo.util.config_util import get_config_value
from elo.util.rating_util import update_elos, update_stats

from elo.model.match import Match

from elo.service import player_service


@click.command(no_args_is_help=True, help="Add a match to the active series.")
@click.argument("home_name", type=str)
@click.argument("home_score", type=int)
@click.argument("away_score", type=int)
@click.argument("away_name", type=str)
@click.option(
    "-s",
    "--sd",
    is_flag=True,
    required=False,
    show_default=True,
    help="Indicate the match went to sudden death.",
)
@click.help_option("-h", "--help")
def add_match(
    home_name: str, home_score: int, away_score: int, away_name: str, sd: bool
):
    """Add a match to the active series.

    Args:
        home_name (str): name of the home player
        home_score (int): score of the home player
        away_score (int): score of the away player
        away_name (str): name of the away player
        sd (bool): sudden death
    """
    # TODO: check if series already exists
    active_series = get_config_value("active-series")
    active_db = db_init(active_series)

    db_connect(active_db)

    # query for existing player data
    home_player = player_service.get_by_name(home_name)
    if not home_player:
        print(f"Player '{home_name}' does not exist. Match cannot be recorded.")
        print(f"\tRun 'elo player add {home_name}' to add.")
        exit()

    away_player = player_service.get_by_name(away_name)
    if not away_player:
        print(f"Player '{away_name}' does not exist. Match cannot be recorded.")
        print(f"\tRun 'elo player add {away_name}' to add.")
        exit()

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
    print("Match recorded.")

    db_close(active_db)
