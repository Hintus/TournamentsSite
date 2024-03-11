import datetime
import enum

from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, Table, MetaData, text, Enum
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.sql.annotation import Annotated

intpk = Annotated[int, mapped_column(primary_key=True)]
metadata = MetaData()


# class Tournament_type(enum.Enum):
#     all_vs_all = 'all_vs_all'
#     play_off = 'play_off'
#     groups = 'groups'

class Tournament_type(enum.Enum):
    all_vs_all = 'all_vs_all'
    play_off = 'play_off'
    groups = 'groups'


# class Tournament(Base):
#     __tablename__ = 'tournament'
#     id: Mapped[intpk]
#     name: Mapped[str]
#     is_ended: Mapped[bool]
#     type: Mapped[Tournament_type]
#     # games: Mapped[]

Tournament = Table(
    "tournament",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('is_ended', Boolean),
    Column('type', Enum(Tournament_type)),
    Column('started_at', TIMESTAMP),
    Column('ended_at', TIMESTAMP, nullable=True),
)

# class Game_type(enum.Enum):
#     dota2 = 'dota2'
#     cs2 = 'cs2'
#     hearthstone = 'hearthstone'


# class Game(Base):
#     __tablename__ = 'game'
#     id: Mapped[intpk]
#     tournament_id: Mapped[int] = mapped_column(ForeignKey("tournament.id", ondelete=CASCADE))
#     type: Mapped[Game_type]
#     # players : Mapped[]

Game = Table(
    "game",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("game_type", String),
    Column("teams_id", Integer),
    Column("started_at", TIMESTAMP),
    Column("ended_at", TIMESTAMP)
)

# class Team(Base):
#     __tablename__ = 'team'
#     id: Mapped[intpk]
#     playing_in: Mapped[int] = mapped_column(ForeignKey("tournament.id", ondelete=CASCADE))
#     # played_in: Mapped[]

Team = Table(
    "team",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("created_at", TIMESTAMP, server_default=text("TIMEZONE('utc', now())")),
    Column("updated_at", TIMESTAMP, server_default=text("TIMEZONE('utc', now())"), onupdate=datetime.datetime.utcnow),
)
