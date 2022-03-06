from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/api/v1/first")
async def root():
    data = 10
    return data

@app.get("/api/v1/plus/{num_1}/{num_2}")
async def plus(num_1: int, num_2: int):
    result = int(num_1) + int(num_2)
    return result

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