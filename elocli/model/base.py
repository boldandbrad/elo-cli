
from peewee import *

# from elocli.util.db_util import db
db = SqliteDatabase(None)


class Base(Model):
    """Base peewee database model class."""

    def __repr__(self):
        return str(self.__dict__)

    def __str__(self):
        return str(self.__dict__)

    class Meta():
        """Define database table options."""
        # database = db
        legacy_table_names = False
