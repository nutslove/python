from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/{animal}")
async def main(animal: str):
    ## ""の中に{}で変数を定義するためには""の前に「f」を付ける必要がある
    image_file = f"static/{animal}.jpg"
    return FileResponse(image_file)