from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse
from typing import Optional

app = FastAPI()

@app.get("/api/v1/first")
async def root():
    data = 10
    return data

@app.get("/api/v1/plus")
async def plus(num_1: int = 10, num_2: int = 90):
    result = num_1 + num_2
    return result

@app.get("/api/v1/title")
async def plus(title: Optional[str] = None):
    return title

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