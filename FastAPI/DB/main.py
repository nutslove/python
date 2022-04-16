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

## 一部のデータを修正するためにputよりpatchが良い？下記URL参照
# https://fastapi.tiangolo.com/tutorial/body-updates/?h=+par#partial-updates-with-patch
@app.patch("/cat/{name}", response_model=schemas.AnimalBase)
def update_animal(name: str, breed: str, sex: str, age: int, owner: str, cat: schemas.AnimalBase, db: Session = Depends(get_db)):
    cat = crud.get_cat(db, cat_name=name)
    if cat is None:
        raise HTTPException(status_code=404, detail=f"Cat[{name}] not fount")
    cat_info = {
        "name": name,
        "breed": breed,
        "sex": sex,
        "age": age,
        "owner": owner
    }
    return crud.update_cat(db=db, cat=cat_info)

@app.post("/dog/{name}", response_model=schemas.AnimalBase)
def create_animal(name: str, breed: str, sex: str, age: int, owner: str, dog: schemas.AnimalBase, db: Session = Depends(get_db)):
    dog = crud.get_dog(db, dog_name=name)
    if dog:
        raise HTTPException(status_code=400, detail=f"Dog[{name}] already registered")
    dog_info = {
        "name": name,
        "breed": breed,
        "sex": sex,
        "age": age,
        "owner": owner
    }
    return crud.create_dog(db=db, dog=dog_info)

@app.get("/dog/{name}", response_model=schemas.AnimalBase)
def get_animal(name: str,db: Session = Depends(get_db)):
    dog = crud.get_dog(db, dog_name=name)
    if dog is None:
        raise HTTPException(status_code=404, detail=f"Dog[{name}] not found")
    return dog

@app.delete("/dog/{name}", response_model=schemas.AnimalBase)
def delete_animal(name: str,db: Session = Depends(get_db)):
    dog = crud.get_dog(db, dog_name=name)
    if dog is None:
        raise HTTPException(status_code=404, detail=f"Dog[{name}] not found")
    return crud.delete_dog(db, dog_name=name)

@app.patch("/dog/{name}", response_model=schemas.AnimalBase)
def update_animal(name: str, breed: str, sex: str, age: int, owner: str, dog: schemas.AnimalBase, db: Session = Depends(get_db)):
    dog = crud.get_dog(db, dog_name=name)
    if dog is None:
        raise HTTPException(status_code=404, detail=f"Dog[{name}] not fount")
    dog_info = {
        "name": name,
        "breed": breed,
        "sex": sex,
        "age": age,
        "owner": owner
    }
    return crud.update_dog(db=db, dog=dog_info)