import enum
from tkinter import CASCADE

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.sql.annotation import Annotated

from src.auth.database import Base

intpk = Annotated[int, mapped_column(primary_key=True)]


class Tournament_type(enum.Enum):
    all_vs_all = 'all_vs_all'
    play_off = 'play_off'
    groups = 'groups'


class Tournament(Base):
    __tablename__ = 'tournament'
    id: Mapped[intpk]
    name: Mapped[str]
    is_ended: Mapped[bool]
    type: Mapped[Tournament_type]
    # games: Mapped[]


class Game_type(enum.Enum):
    dota2 = 'dota2'
    cs2 = 'cs2'
    hearthstone = 'hearthstone'


class Game(Base):
    __tablename__ = 'game'
    id: Mapped[intpk]
    tournament_id: Mapped[int] = mapped_column(ForeignKey("tournament.id", ondelete=CASCADE))
    type: Mapped[Game_type]
    # players : Mapped[]


class Team(Base):
    __tablename__ = 'team'
    id: Mapped[intpk]
    playing_in: Mapped[int] = mapped_column(ForeignKey("tournament.id", ondelete=CASCADE))
    # played_in: Mapped[]
