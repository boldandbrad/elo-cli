
import datetime

from peewee import *

from .base import Base
from .player import Player


class Match(Base):
    """Database schema for Match table."""
    home_player = ForeignKeyField(Player, backref="matches")
    away_player = ForeignKeyField(Player, backref="matches")
    home_score = IntegerField(default=0)
    away_score = IntegerField(default=0)
    sudden_death = BooleanField(default=False)
    rating_change = FloatField(default=0)
    number = IntegerField(default=100000)
    date = DateTimeField(default=datetime.datetime.now)
