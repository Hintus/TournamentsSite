from datetime import datetime

from pydantic import BaseModel


# class TournamentCreate(BaseModel):
#     id: int
#     name: str
#     is_ended: bool
#     type: ...
#     started_at: datetime
#     ended_at: datetime


class GameCreate(BaseModel):
    id: int
    game_type: str
    teams_id: int
    started_at: datetime
    ended_at: datetime
