
import click

from .util.log_util import log_init
from .util.config_util import config_init

from .command.series_grp.series import series
from .command.player_grp.player import player
from .command.match_grp.match import match


@click.group(
    help='Calculate ELO ratings in your terminal.'
)
@click.help_option(
    '-h', '--help'
)
@click.version_option(
    None,  # use version auto discovery via setuptools
    '-v', '--version',
    message='%(prog)s-cli, v%(version)s'
)
def cli():
    """Main 'elo' command group.
    """

    log_init()
    config_init()


cli.add_command(series, 'series')
cli.add_command(player, 'player')
cli.add_command(match, 'match')

if __name__ == "__main__":
    cli()
