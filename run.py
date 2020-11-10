# サーバー立ち上げ用
from urls import app
import uvicorn

if __name__ == '__main__':
    # & uvicorn run:app --reloadをターミナルで打っても可
    uvicorn.run(app=app, port=8888)