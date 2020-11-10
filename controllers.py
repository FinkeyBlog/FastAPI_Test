# レスポンス処理用
from fastapi import FastAPI
from starlette.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI(
    title='FastAPI Sample APP',
    description='Create FastAPI App',
    version='0.0.1'
)

# テンプレート関連の設定 (jinja2)
templates = Jinja2Templates(directory="templates")
jinja_env = templates.env  # Jinja2.Environment : filterやglobalの設定用
 
def index(request: Request):
    return templates.TemplateResponse('index.html',
                                      {'request': request,
                                      'test':'テスト'})