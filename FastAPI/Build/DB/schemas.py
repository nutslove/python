## 利用者側から送られてくるDBクエリーの構造
from pydantic import BaseModel

class AnimalBase(BaseModel):
    name: str
    breed: str
    sex: str
    age: int
    owner: str

    class Config:
        orm_mode = True