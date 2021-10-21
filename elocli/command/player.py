
import click
from loguru import logger

from elocli.command.player_cmds.add import add_player
from elocli.command.player_cmds.list import list_players


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
