from fastapi import FastAPI, Depends
from fastapi_users import FastAPIUsers
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

from src.auth.auth import auth_backend
from src.auth.database import User
from src.auth.manager import get_user_manager
from src.auth.schemas import UserRead, UserCreate
from src.auth.router import router as router_login
from src.classes.router import router as router_classes
from src.main.router import router as router_pages

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

current_user = fastapi_users.current_user()


@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"
