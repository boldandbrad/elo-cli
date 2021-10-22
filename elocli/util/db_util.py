from os import path, walk

from typing import List
from peewee import SqliteDatabase

from elocli.model.match import Match
from elocli.model.player import Player

from elocli.util.env_util import get_db_path


def db_init(name: str):
    db = SqliteDatabase(None)

    db_path = get_db_path()
    db.bind([Player, Match])
    db.init(db_path + "/" + name + ".db", pragmas={"foreign_keys": 1})
    with db:
        db.create_tables([Player, Match])
    return db


def db_connect(db: SqliteDatabase):
    db.connect()


def db_close(db: SqliteDatabase):
    db.close()


def get_dbs() -> List[str]:
    db_path = get_db_path()
    db_files = next(walk(db_path))[2]
    for idx, db_file in enumerate(db_files):
        db_files[idx] = path.splitext(db_file)[0]
    return db_files
