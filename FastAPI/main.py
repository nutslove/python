from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"Hello": "Lee! Keep going!!!"}

@app.get("/param_int/{item_id}")
async def read_item(item_id: int): # FastAPIは自動でValidationチェックまでしてくれて、pythonでは型の強制力はなかった(int以外の型が入ってもエラーにならない)気がするが、FastAPIの場合実際int以外の型の値が入るとエラーになる。
    return {"int_item_id": item_id}