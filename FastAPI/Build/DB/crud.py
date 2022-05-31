from io import BufferedReader
from sqlalchemy.orm.session import Session
import schemas, models

def create_cat(db: Session, cat: schemas.AnimalBase):
    new_cat = models.Cat_Data(
        name = cat['name'],
        breed = cat['breed'],
        sex = cat['sex'],
        age = cat['age'],
        owner = cat['owner']
    )
    db.add(new_cat)
    db.commit()
    db.refresh(new_cat)
    return new_cat

def get_cat(db: Session, cat_name: str):
    return db.query(models.Cat_Data).filter(models.Cat_Data.name == cat_name).first()

def delete_cat(db: Session, cat_name: str):
    db.query(models.Cat_Data).filter(models.Cat_Data.name == cat_name).delete()
    db.commit()
    # ここでreturnするとschemaのvalidationでエラーになる。name以外のbreed,age等が戻り値にないため。

def update_cat(db: Session, cat: schemas.AnimalBase):
    update_cat = models.Cat_Data(
        name = cat['name'],
        breed = cat['breed'],
        sex = cat['sex'],
        age = cat['age'],
        owner = cat['owner']
    )
    # mergeだとprimary key(主キー)による(マッチする)レコードのupdateしかできない？
    # https://stackoverflow.com/questions/63143731/update-sqlalchemy-orm-existing-model-from-posted-pydantic-model-in-fastapi
    update_obj = db.merge(update_cat)
    db.add(update_obj)
    db.commit()
    db.refresh(update_obj)
    return update_obj

def create_dog(db: Session, dog: schemas.AnimalBase):
    new_dog = models.Dog_Data(
        name = dog['name'],
        breed = dog['breed'],
        sex = dog['sex'],
        age = dog['age'],
        owner = dog['owner']
    )
    db.add(new_dog)
    db.commit()
    db.refresh(new_dog)
    return new_dog

def get_dog(db: Session, dog_name: str):
    return db.query(models.Dog_Data).filter(models.Dog_Data.name == dog_name).first()

def delete_dog(db: Session, dog_name: str):
    db.query(models.Dog_Data).filter(models.Dog_Data.name == dog_name).delete()
    db.commit()
    # ここでreturnするとschemaのvalidationでエラーになる。name以外のbreed,age等が戻り値にないため。

def update_dog(db: Session, dog: schemas.AnimalBase):
    update_dog = models.Dog_Data(
        name = dog['name'],
        breed = dog['breed'],
        sex = dog['sex'],
        age = dog['age'],
        owner = dog['owner']
    )
    # mergeだとprimary key(主キー)による(マッチする)レコードのupdateしかできない？
    # https://stackoverflow.com/questions/63143731/update-sqlalchemy-orm-existing-model-from-posted-pydantic-model-in-fastapi
    update_obj = db.merge(update_dog)
    db.add(update_obj)
    db.commit()
    db.refresh(update_obj)
    return update_obj