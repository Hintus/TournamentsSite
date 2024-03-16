from schemas import STournamentAdd
from src.auth.database import get_async_session
from src.classes.models import Tournament


class TournamentRepository:
    @classmethod
    async def add_one(cls, data: STournamentAdd) -> int:
        async with get_async_session() as session:
            tournament_dict = data.model_dump()

            new_tournament = Tournament(**tournament_dict)

            session.add(new_tournament)
            await session.flush()
            await session.execute()
            return new_tournament.id

