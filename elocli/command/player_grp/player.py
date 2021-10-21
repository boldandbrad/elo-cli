
import click
# from loguru import logger

from .command.add import add_player
from .command.list import list_players


@click.group(
    help='Manage players in the active series.'
)
@click.help_option(
    '-h', '--help'
)
def player():
    pass


player.add_command(add_player, 'add')
player.add_command(list_players, 'list')
# player.add_command(stats_player, 'stats')
