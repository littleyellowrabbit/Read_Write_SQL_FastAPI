from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase

class SQLBase(DeclarativeBase):
    pass

class User(SQLBase):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

