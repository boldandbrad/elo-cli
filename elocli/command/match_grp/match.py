import click

# from loguru import logger

from .command.add import add_match
from .command.list import list_matches


@click.group(help="Manage matches in the active series.")
@click.help_option("-h", "--help")
def match():
    pass


match.add_command(add_match, "add")
match.add_command(list_matches, "list")
