from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse
from typing import Optional
from io import BytesIO
from PIL import Image
import httpx
import time

app = FastAPI()

@app.get("/api/v1/calculate", status_code=503)
def plus(operator:str = "", num_1: int = 10, num_2: int = 90): ## parameterとして定義したもの(ex. operator)は初期値を定義しておく必要がある。(でないとエラーになる)
    if operator == "addition":
        result = num_1 + num_2
    elif operator == "multiplication":
        result = num_1 * num_2
    else:
        result = 77

    title = "猫と足し算の部屋"
    calculation = "足し算"

    db_url = "http://db.default.svc.cluster.local/cat/Ruka"
    db = httpx.get(db_url)
    return result, {"title": title, "calculation": calculation}, "cat", db.text

@app.get("/api/v1/image/{animal}")
def image_get(animal: str):
    # image_url = "http://172.31.43.217:8080/api/v1/cat"
    image_url = "http://image.default.svc.cluster.local/api/v1/" + animal
    image = httpx.get(image_url)
    image = Image.open(BytesIO(image.content))
    image.save(f"static/{animal}.jpg")
    image_file = f"static/{animal}.jpg"
    return FileResponse(image_file)