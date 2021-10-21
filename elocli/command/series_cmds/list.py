
from os import path, walk

import click

# from elocli.util.db_util import db_init
from elocli.util.config_util import get_config_value
from elocli.util.env_util import get_db_path

# from elocli.model.base import db


@click.command(
    help='List all created series.'
)
@click.help_option(
    '-h', '--help'
)
def list_series():
    active_series = get_config_value('active-series')
    db_path = get_db_path()
    # active_db = db_init(db, active_series)

    db_files = next(walk(db_path))[2]

    for db_file in db_files:
        name = path.splitext(db_file)[0]
        if name == active_series:
            print(f'{name} (active)')
        else:
            print(name)
