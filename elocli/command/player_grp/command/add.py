import click

from elocli.util.db_util import db_init, db_connect, db_close
from elocli.util.config_util import get_config_value

from elocli.service.player_service import get_or_create_by_name


@click.command(help="Add a player to the active series.")
@click.help_option("-h", "--help")
@click.argument("name", required=True)
def add_player(name: str):
    # TODO: check if series already exists
    active_series = get_config_value("active-series")
    active_db = db_init(active_series)

    db_connect(active_db)

    _ = get_or_create_by_name(name)

    db_close(active_db)
