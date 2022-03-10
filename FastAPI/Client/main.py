from enum import Enum
import httpx
import json
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse ## Requestに対してResponseとしてHTMLを返す
from fastapi.staticfiles import StaticFiles # 
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse ## Requestに対してResponseとしてファイルを返す # aiofilesのインストールが必要(pip3 install aiofiles)

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

@app.get("/photo")
def photo():
    return FileResponse("static/BrooklynBridge-1.jpg") # このmain.pyがあるディレクトリから相対パス

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
#    title_url = "http://172.31.32.49:8080/api/v1/title?title=What Should I do?"
    title_url = "http://172.31.32.49:8080/api/v1/title"
    title = httpx.get(title_url)
    # print("Header: ", title.headers) # httpx.getで取得した「オブジェクト.headers」にHTTPヘッダの情報が入っている
    # print("URL: ", title.url) # httpx.getで取得した「オブジェクト.url」にURL情報が入ってる
    # print("Status Code: ", title) # httpx.getで取得したオブジェクトにはステータスコードが入ってる
    jsondata = json.loads(title.text)
    title = jsondata['title']
    calculation = jsondata['calculation']
    result = "数字を入力して下さい"
    return templates.TemplateResponse("root.html",{"request": request, "result": result, "title": title, "calculation": calculation})

@app.post("/plus", response_class=HTMLResponse)
async def plus(request: Request, num1: int = Form(...), num2: int = Form(...)):
    url = f'http://172.31.32.49:8080/api/v1/plus?num_1={num1}&num_2={num2}'
    result = httpx.get(url)

    title_url = "http://172.31.32.49:8080/api/v1/title"
    title = httpx.get(title_url)
    jsondata = json.loads(title.text)
    title = jsondata['title']
    calculation = jsondata['calculation']

    return templates.TemplateResponse("root.html",{"request": request, "result": result.text, "title": title, "calculation": calculation})