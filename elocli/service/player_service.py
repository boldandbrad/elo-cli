from typing import List, Tuple

from peewee import DoesNotExist

from elocli.model.player import Player
# from elocli.util import out_util


def get_all_ordered() -> List[Player]:
    """Retrieve all players ordered by rank field."""
    try:
        return Player.select().order_by(-Player.rank)
    except DoesNotExist as dne:
        # TODO: log error
        return []


# def get_by_id(id: int) -> Player:
#     """Retrieve a player by its id field."""
#     return Player.get().where(Player.id == id)


def get_by_name(name: str) -> Player:
    """Retrieve a player by its name field."""
    return Player.select().where(Player.name == name).get()


def get_or_create_by_name(name: str) -> Player:
    """Retrieve a player by its name field, create if does not exist."""
    player, created = Player.get_or_create(name=name)
    if created:
        # out_util.print_player_create(player)
        print(f'added new player: {player.name}')
    else:
        # out_util.print_player_retrieved(player)
        print(f'player already exists: {player.name}')
    return player


def save(player: Player):
    """Persist new player to database."""
    player.save()