from fastapi import FastAPI
from fastapi_users import FastAPIUsers
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

from auth.auth import auth_backend
from auth.database import User
from auth.manager import get_user_manager
from auth.schemas import UserRead, UserCreate
from pages.router import router as router_pages
from auth.router import router as router_login
from classes.router import router as router_classes

app = FastAPI()

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


app.include_router(router_pages)
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

