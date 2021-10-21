
from peewee import SqliteDatabase

from elocli.model.match import Match
from elocli.model.player import Player

from elocli.util.env_util import get_db_path


# contact config to get db path
# create db from config

def db_init(db: SqliteDatabase, name: str):
    db_path = get_db_path()
    db.bind([Player, Match])
    db.init(db_path + '/' + name + '.db', pragmas={'foreign_keys': 1})
    with db:
        db.create_tables([Player, Match])
    return db

def db_connect(db: SqliteDatabase):
    db.connect()

def db_close(db: SqliteDatabase):
    db.close()

def get_dbs():
    pass
