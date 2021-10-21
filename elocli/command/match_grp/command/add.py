
from typing import Optional, Tuple

import click

from elocli.util.db_util import db_init, db_connect, db_close
from elocli.util.config_util import get_config_value

from elocli.model.match import Match

from elocli.service import player_service
from elocli.service import match_service


@click.command(
    help='Add a match to the active series.'
)
@click.help_option(
    '-h', '--help'
)
@click.argument(
    'home',
    nargs=2
)
@click.argument(
    'away',
    nargs=2,
)
@click.option(
    '-s', '--sd',
    is_flag=True,
    required=False
)
def add_match(home: Tuple[str, int], away: Tuple[str, int], sd: bool):
    # TODO: check if series already exists
    active_series = get_config_value('active-series')
    active_db = db_init(active_series)

    db_connect(active_db)

    home_score = int(home[1])
    away_score = int(away[1])

    # TODO: check if players do not yet exist
    home_player = player_service.get_by_name(home[0])
    away_player = player_service.get_by_name(away[0])

    # TODO: update player elos based on outcome
    rating_change = 0

    # TODO: update player stats based on outcome


    home_player.save()
    away_player.save()

    match = Match(
        home_player=home_player.id,
        away_player=away_player.id,
        home_score=home_score,
        away_score=away_score,
        sudden_death=sd,
        rating_change=rating_change
    )

    match.save()
    print('match recorded')

    db_close(active_db)
