from fastapi import APIRouter, Request, Depends
from select import select
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates
from src.auth.database import get_async_session
from src.classes.models import *
from src.classes.schemas import GameCreate

router = APIRouter(
    prefix='/classes',
    tags=['classes']
)

templates = Jinja2Templates(directory="templates")


@router.get('/users', response_class=HTMLResponse)
async def users(request: Request):
    return templates.TemplateResponse(request=request, name='classes/users.html')


@router.get('/teams', response_class=HTMLResponse)
async def teams(request: Request):
    return templates.TemplateResponse(request=request, name='classes/teams.html')


@router.get('/tournaments', response_class=HTMLResponse)
async def tournaments_page(request: Request):
    return templates.TemplateResponse(request=request, name='classes/tournaments.html')


@router.get('/tournaments/all_vs_all', response_class=HTMLResponse)
async def tournaments_all_vs_all(request: Request):
    return templates.TemplateResponse(request=request, name='classes/tournaments/all_vs_all.html')


@router.get('/')
async def get_all_tournaments(id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(Tournament).where(Tournament.c.id == id)
    result = await session.execute(query)
    return result.all()


@router.post("/")
async def add_game(new_game: GameCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Game).values(**new_game.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
