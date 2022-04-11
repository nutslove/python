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