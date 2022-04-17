from enum import Enum
import httpx
import json
from io import BytesIO
from PIL import Image
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

title = ""
calculation = ""
animal_type = ""
name = ""
breed = ""
sex = ""
age = ""
owner = ""

@app.get("/", response_class=HTMLResponse)
async def plus(request: Request):

    global title
    global calculation
    global animal_type
    global name
    global breed
    global sex
    global age
    global owner

    url = "http://calculate.default.svc.cluster.local/api/v1/calculate"
    results = httpx.get(url)
    # print("Header: ", title.headers) # httpx.getで取得した「オブジェクト.headers」にHTTPヘッダの情報が入っている
    # print("URL: ", title.url) # httpx.getで取得した「オブジェクト.url」にURL情報が入ってる
    # print("Status Code: ", title) # httpx.getで取得したオブジェクトにはステータスコードが入ってる
    # cal_result = json.loads(results.text)[0] # getの時はcal_resultは使わない
    jsondata = json.loads(results.text)[1]
    title = jsondata['title']
    calculation = jsondata['calculation']
    result = "数字を入力して下さい"
    # image_url = "http://172.31.32.49:8080/api/v1/image"
    animal_type = json.loads(results.text)[2]
    image_url = "http://calculate.default.svc.cluster.local/api/v1/image/" + animal_type
    image = httpx.get(image_url)
    image = Image.open(BytesIO(image.content))
    image.save(f"static/{animal_type}.jpg")
    animal = json.loads(results.text)[3]
    name = json.loads(animal)['name']
    breed = json.loads(animal)['breed']
    sex = json.loads(animal)['sex']
    age = json.loads(animal)['age']
    owner = json.loads(animal)['owner']

    return templates.TemplateResponse("root.html",{"request": request, "result": result, "title": title, "calculation": calculation, "animal_type": animal_type, "name": name, "breed": breed, "sex": sex, "age": age, "owner": owner})

@app.post("/", response_class=HTMLResponse)
async def plus(request: Request, num1: int = Form(...), num2: int = Form(...)):

    if animal_type == "cat":
        operator = "addition"
    elif animal_type == "dog":
        operator = "multiplication"
    url = f'http://calculate.default.svc.cluster.local/api/v1/calculate?operator={operator}&num_1={num1}&num_2={num2}'
    results = httpx.get(url)

    result = json.loads(results.text)[0]

    return templates.TemplateResponse("root.html",{"request": request, "result": result, "title": title, "calculation": calculation, "animal_type": animal_type, "name": name, "breed": breed, "sex": sex, "age": age, "owner": owner})