from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

router = APIRouter(
    prefix='/pages',
    tags=['Pages']
)

templates = Jinja2Templates(directory="templates")


@router.get('/', response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse(request=request, name='main.html')


@router.get('/schemas', response_class=HTMLResponse)
async def schemas(request: Request):
    return templates.TemplateResponse(request=request, name='schemas_main.html')
