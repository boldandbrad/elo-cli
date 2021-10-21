
import click

# from elocli.util.db_util import db_init
from elocli.util.config_util import set_config_value

# from elocli.model.base import db

@click.command(
    help='Activate an existing series.'
)
@click.help_option(
    '-h', '--help'
)
@click.argument('name', required=True)
def set_series(name: str):
    # TODO: check if series exists before setting
    set_config_value('active-series', name)
    print('set active series: ' + name)
