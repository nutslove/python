from enum import Enum
from fastapi import FastAPI

class ModelName(str, Enum):
    Lee = "Joonki"
    Kim = "Su"
    Park = "Min"

app = FastAPI()

@app.get("/")
async def root():
    return {"Hello": "Lee! Keep going?????!!!"}

@app.get("/param_int/{item_id}")
async def read_item(item_id: int): # FastAPIは自動でValidationチェックまでしてくれて、pythonでは型の強制力はなかった(int以外の型が入ってもエラーにならない)気がするが、FastAPIの場合実際int以外の型の値が入るとエラーになる。
    return {"int_item_id": item_id}

@app.get("/model/{model_name}")
async def model(model_name: ModelName): #上のModelNameクラスの下の"="の後ろに定義した値(このケースだと"Joonki","Su","Min")だけを受け付ける（それ以外はエラーとなる）
    if model_name == "Joonki":
        return {"LastName": "Lee"}
    else:
        return "I don't know that model."
