from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse
from typing import Optional
from io import BytesIO
from PIL import Image
import httpx

app = FastAPI()

@app.get("/api/v1/calculate")
def plus(num_1: int = 10, num_2: int = 90):
    result = num_1 + num_2
    return result

@app.get("/api/v1/title")
def title(title: Optional[str] = None, title_color: Optional[str] = None):
    title = "猫と足し算の部屋"
    calculation = "足し算"
    return {"title": title, "calculation": calculation}

@app.get("/api/v1/image")
def image_get():
    # image_url = "http://172.31.43.217:8080/api/v1/cat"
    image_url = "http://image.default.svc.cluster.local/api/v1/cat"
    image = httpx.get(image_url)
    image = Image.open(BytesIO(image.content))
    image.save("static/animal.jpg")
    image_file = "static/animal.jpg"
    return FileResponse(image_file)

@app.get("/api/v1/db")
def db_get():
    # db_url = "http://3.112.2.208:8080/cat/Ruka"
    db_url = "http://db.default.svc.cluster.local/cat/Ruka"
    db = httpx.get(db_url)
    return db.text

@app.get("/")
async def root():
    data = """<?xml version="1.0"?>
    <shampoo>
    <Header>
        Apply shampoo here.
    </Header>
    <Body>
        You'll have to use soap here.
    </Body>
    </shampoo>
    """
    return Response(content=data, media_type="application/xml")