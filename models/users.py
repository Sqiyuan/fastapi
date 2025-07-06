from models import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    username = Column(String(50), unique=True, index=True)
    password = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, index=True)

class UserExtension(Base):
    __tablename__ = 'user_extensions'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    university = Column(String(50))
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', backref='extensions', uselist=False)