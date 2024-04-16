from fastapi import FastAPI, Depends, Request
from fastapi_users import FastAPIUsers
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles

from src.auth.auth import auth_backend
from src.auth.database import User
from src.auth.manager import get_user_manager
from src.auth.schemas import UserRead, UserCreate
from src.auth.router import router as router_login
from src.classes.router import router as router_classes


app = FastAPI()

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

# app.include_router(router_pages)
app.include_router(router_login)
app.include_router(router_classes)

app.mount("/static", StaticFiles(directory="static"), name='static')

templates = Jinja2Templates(directory="templates")

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

current_user = fastapi_users.current_user(active=True)


@app.get("/private_route", response_class=HTMLResponse)
def protected_route(request: Request, user: User = Depends(current_user)):
    try:
        user = fastapi_users.current_user(active=True)
        context = {'user': user}
        return templates.TemplateResponse(request=request, name='popa.html', context=context)
    finally:
        return templates.TemplateResponse(request=request, name='popa.html')


@app.get("/popa_route", response_class=HTMLResponse)
def popa_route(request: Request):
    return templates.TemplateResponse(request=request, name='popa.html')


@app.get('/', response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse(request=request, name='main.html')


@app.get('/schemas', response_class=HTMLResponse)
async def schemas(request: Request):
    return templates.TemplateResponse(request=request, name='schemas_main.html')
