# from schemas import STournamentAdd
from fastapi import Depends
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.database import get_async_session
from src.classes.models import Tournament
from src.classes.schemas import STournamentAdd


class TournamentRepository:
    @classmethod
    async def add_one(cls, data: STournamentAdd, session: AsyncSession = Depends(get_async_session)):
        tournament_dict = data.model_dump()

        new_tournament = Tournament(**tournament_dict)
        querry = insert(new_tournament)
        session.add(new_tournament)
        await session.flush()
        await session.execute(querry)
        return new_tournament.id
