from enum import Enum
import httpx
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

class ModelName(str, Enum):
    Lee = "Joonki"
    Kim = "Su"
    Park = "Min"

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return_message = httpx.get('http://172.31.32.49:8080/api/v1/first')
    print(return_message) # <Response [200 OK]>や<Response [404 Not Found]>など、ステータスコードが格納されている
    print(return_message.text) # 中身を取り出したいときは「.text」を付ける必要があるっぽい
    print(type(return_message))
    return "ID: " + return_message.text

@app.get("/param_int/{item_id}")
async def read_item(item_id: int): # FastAPIは自動でValidationチェックまでしてくれて、pythonでは型の強制力はなかった(int 以外の型が入ってもエラーにならない)気がするが、FastAPIの場合実際int以 外の型の値が入るとエラーになる。
    return {"int_item_id": item_id}

@app.get("/model/{model_name}")
async def model(model_name: ModelName): #上のModelNameクラスの下の"="の後ろに定義した値(このケースだと"Joonki","Su","Min")だけを受け付ける（それ以外はエラーとなる）
    if model_name == "Joonki":
        return {"LastName": "Lee"}
    else:
        return "I don't know that model."

@app.get("/plus", response_class=HTMLResponse)
async def plus(request: Request):
    result = "計算してください"
    return templates.TemplateResponse("root.html",{"request": request, "result": result})

@app.post("/plus", response_class=HTMLResponse)
async def plus(request: Request, num1: int = Form(...), num2: int = Form(...)):
    url = 'http://172.31.32.49:8080/api/v1/plus/' + str(num1) + '/' + str(num2)
    result = httpx.get(url)
    result = result.text
    return templates.TemplateResponse("root.html",{"request": request, "result": result})