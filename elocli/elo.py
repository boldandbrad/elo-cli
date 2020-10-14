
import click


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
    pass


if __name__ == "__main__":
    cli()