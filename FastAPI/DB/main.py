from fastapi import FastAPI, Response
import models
from database import engine

db = FastAPI()

models.Base.metadata.create_all(engine) # models.pyで定義したテーブル構造でdatabase.pyに定義したDBファイル名でDBを作成