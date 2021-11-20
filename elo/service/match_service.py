"""Database Match Service"""

from typing import List

from peewee import DoesNotExist

from elo.model.match import Match


def get_all_ordered() -> List[Match]:
    """Retrieve all matches ordered by number field."""
    try:
        return Match.select().order_by(+Match.number)
    except DoesNotExist:
        # TODO: log error
        return []


# def get_all_by_player(player_id: int) -> List[Match]:
#     """Retrieve all of a player's matches by player id field."""
#     return Match.select().where(Match.home_player_id == player_id |
#                                 Match.away_player_id == player_id)


# def get_by_id(id: int) -> Match:
#     """Retrieve a match by its id field."""
#     return Match.select().where(Match.id == id).get()


def get_by_number(number: int) -> Match:
    """Retrieve a match by its number field."""
    return Match.select().where(Match.number == number).get()


def save(match: Match) -> Match:
    """Persist new match to database."""
    match.save()
