from peewee import CharField, FloatField, IntegerField

from .base import Base


class Player(Base):
    """Database schema for Player table."""

    name = CharField(unique=True)
    elo = FloatField(default=1000.0)
    rank = IntegerField(default=0)
    wins = IntegerField(default=0)
    draws = IntegerField(default=0)
    losses = IntegerField(default=0)
    goals_for = IntegerField(default=0)
    goals_against = IntegerField(default=0)
