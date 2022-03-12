from io import BufferedReader
from sqlalchemy.orm.session import Session
from schemas import CatUSerBase
from models import Cat_Data

def create_cat(db: Session, request: CatUSerBase):
    new_cat = Cat_Data(
        catname = request.catname
        breed = request.breed
        sex = request.sex
        age = request.age
        owner = request.owner
    )
    db.add(new_cat)
    db.commit()
    db.refresh(new_cat)
    return new_cat