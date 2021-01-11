from sqlalchemy import Column, Integer, String, Boolean
from repository.mysql import Base


class Example(Base):
    __tablename__ = 'example'

    exampleId = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True, index=True)
    is_active = Column(Boolean, default=True)


class Item(Base):
    __tablename__ = 'items'

    itemId = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False, default="")
