
import click

from elocli.util.log_util import log_init
from elocli.util.config_util import config_init

from elocli.command.series import series
from elocli.command.player import player


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

if __name__ == "__main__":
    cli()
