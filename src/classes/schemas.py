from datetime import datetime
from enum import Enum, IntEnum
from typing import Optional

from pydantic import BaseModel, ConfigDict


class GameCreate(BaseModel):
    id: int
    game_type: str
    teams_id: int
    started_at: datetime
    ended_at: datetime


class TournamentTypeEnum(str, Enum):
    all_vs_all = 'all_vs_all'
    play_off = 'play_off'
    groups = 'groups'


class STournamentAdd(BaseModel):
    name: str
    is_ended: bool
    type: Optional[TournamentTypeEnum] = None
    started_at: Optional[datetime] = None
    ended_at: Optional[datetime] = None


class STournament(STournamentAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)


class STournamentID(BaseModel):
    ok: bool = True
    id: int
