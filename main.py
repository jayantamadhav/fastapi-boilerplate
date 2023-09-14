from db import settings, models

from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from tortoise.contrib.fastapi import register_tortoise
from decouple import config

SERVER_PREFIX = "/v1"
BASE_DIR = Path(__file__).resolve(strict=True).parent


def register_views(app: FastAPI) -> None:
    from app.auth.router import auth_routes
    from app.users.router import users_routes

    app.include_router(auth_routes, prefix=SERVER_PREFIX + "/auth", tags=["Auth"])
    app.include_router(users_routes, prefix=SERVER_PREFIX + "/users", tags=["Users"])
    
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    openapi_url=SERVER_PREFIX + "/openapi.json",
    docs_url=SERVER_PREFIX + "/docs",
    redoc_url=SERVER_PREFIX + "/redoc",
    debug=True if config("SERVER") != "production" else False,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_views(app=app)
# register_tortoise(
#     app,
#     db_url=settings.DATABASE_URL,
#     modules={"models": models},
#     generate_schemas=True,
#     add_exception_handlers=True,
# )