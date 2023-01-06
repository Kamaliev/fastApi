import os.path

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from database.database import Database
from utils import load_module

app = FastAPI()
origins = [
    "*",
    'usurt.site'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def include_routers():
    path = os.path.join(os.path.dirname(__file__), 'routers')
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)) and file.endswith('.py') and not file.startswith('__'):
            module = load_module('routers.{}'.format(file[:-3]))
            try:
                router = getattr(module, 'router')
                app.include_router(router)
            except AttributeError as e:
                pass


@app.on_event('startup')
def startup():
    Database()
    include_routers()
