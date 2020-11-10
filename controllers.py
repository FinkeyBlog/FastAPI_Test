# レスポンス処理用
from fastapi import FastAPI
from starlette.requests import Request

app = FastAPI(
    title='FastAPI Sample APP',
    description='Create FastAPI App',
    version='0.0.1'
)

def index(request:Request):
    return{'Hello':'World'}