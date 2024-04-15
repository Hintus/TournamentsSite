from fastapi import APIRouter, Request, Depends
from starlette.responses import HTMLResponse, RedirectResponse
from starlette.templating import Jinja2Templates

# from main import fastapi_users
from src.auth.database import User

templates = Jinja2Templates(directory="templates")

router = APIRouter(
    prefix='',
    tags=['Pages']
)


@router.get('/', response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse(request=request, name='main.html')


@router.get('/to_start', response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse(request=request, name='main.html')


@router.get('/schemas', response_class=HTMLResponse)
async def schemas(request: Request):
    return templates.TemplateResponse(request=request, name='schemas_main.html')
