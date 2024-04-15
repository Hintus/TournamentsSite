from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse, RedirectResponse
from starlette.templating import Jinja2Templates

router = APIRouter(
    prefix='/log',
    tags=['log']
)

templates = Jinja2Templates(directory="templates/auth")


@router.get('/login', response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse(request=request, name='login.html')


@router.get('/register', response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse(request=request, name='register.html')
