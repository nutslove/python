## DB構造を定義するファイル
from sqlalchemy.sql.sqltypes import Boolean, Integer, String
from database import Base
from sqlalchemy import Column

class Cat_Data(Base): ## class名は任意
    __tablename__ = 'cats' ## tablenameも任意
    catname = Column(String, primary_key=True, index=True)
    breed = Column(String)
    sex = Column(String)
    age = Column(Integer)
    owner = Column(String)