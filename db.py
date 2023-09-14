import os
from fastapi import FastAPI
from tortoise import Tortoise
from pydantic import BaseSettings
from decouple import config


class Settings(BaseSettings):
    APP_NAME: str = "FastAPI"
    APP_VERSION: str = "0.0.1"
    DATABASE_URL: str = config("DATABASE_URL")


settings = Settings()


models_list = [
    "app.admin.models",
]
models = models_list.copy()
models.append("aerich.models")
