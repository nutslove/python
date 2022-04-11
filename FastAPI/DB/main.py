from urllib import response
from fastapi import FastAPI, Depends, HTTPException, Response
from sqlalchemy.orm import Session
import models, schemas, crud
from database import engine, SessionLocal
from typing import List

app = FastAPI()

models.Base.metadata.create_all(engine) # models.pyで定義したテーブル構造でdatabase.pyに定義したDBファイル名でDBを作成

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# @app.post("/cat/{name}", response_model=List[schemas.AnimalBase]) ## Listは複数件の場合っぽい
@app.post("/cat/{name}", response_model=schemas.AnimalBase)
# POST http(s)://<URL>/cat/<cat名前>?breed=<種>&sex=<性別>&age=<年齢>&owner=<飼い主>
def create_animal(name: str, breed: str, sex: str, age: int, owner: str, cat: schemas.AnimalBase, db: Session = Depends(get_db)):
    cat = crud.get_cat(db, cat_name=name)
    if cat:
        raise HTTPException(status_code=400, detail=f"Cat[{name}] already registered")
    cat_info = {
        "name": name,
        "breed": breed,
        "sex": sex,
        "age": age,
        "owner": owner
    }
    return crud.create_cat(db=db, cat=cat_info)

@app.get("/cat/{name}", response_model=schemas.AnimalBase)
def get_animal(name: str,db: Session = Depends(get_db)):
    cat = crud.get_cat(db, cat_name=name)
    if cat is None:
        raise HTTPException(status_code=404, detail=f"Cat[{name}] not found")
    return cat

@app.delete("/cat/{name}", response_model=schemas.AnimalBase)
def delete_animal(name: str,db: Session = Depends(get_db)):
    cat = crud.get_cat(db, cat_name=name)
    if cat is None:
        raise HTTPException(status_code=404, detail=f"Cat[{name}] not found")
    return crud.delete_cat(db, cat_name=name)

## putの部分要修正。とりあえず追記した感じ
# @app.put("/cat/{name}", response_model=schemas.AnimalBase)
# def update_animal(name: str,db: Session = Depends(get_db)):
#     cat = crud.get_cat(db, cat_name=name)
#     if cat is None:
#         raise HTTPException(status_code=404, detail=f"Cat[{name}] not found")
#     return cat