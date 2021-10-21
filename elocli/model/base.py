
from peewee import *


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
