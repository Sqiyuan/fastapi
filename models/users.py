from models import Base
from sqlalchemy import Column, Integer, String, Text, DateTime

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    username = Column(String(50), unique=True, index=True)
    password = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, index=True)