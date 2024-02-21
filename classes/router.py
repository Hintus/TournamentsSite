from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

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
async def tournaments(request: Request):
    return templates.TemplateResponse(request=request, name='classes/tournaments.html')
