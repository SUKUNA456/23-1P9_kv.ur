"""Отправка html-страницы при помощи FastAPI"""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="public"))
