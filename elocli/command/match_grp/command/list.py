
import click

from elocli.util.db_util import db_init, db_connect, db_close, get_dbs
from elocli.util.config_util import get_config_value

from elocli.service.match_service import get_all_ordered


@click.command(
    help='List all matches in the active series.'
)
@click.help_option(
    '-h', '--help'
)
def list_matches():
    # TODO: check if series already exists
    active_series = get_config_value('active-series')
    active_db = db_init(active_series)

    db_connect(active_db)

    matches = get_all_ordered()
    for match in matches:
        print(match)

    db_close(active_db)
