## 利用者側から送られてくるDBクエリーの構造
from pydantic import BaseModel

class CatUSerBase(BaseModel):
    catname: str
    breed: str
    sex: str
    age: int
    owner: str