from models import Base
from sqlalchemy import ForeignKey, Integer, String, Column, Text
from sqlalchemy.orm import relationship


class Tag(Base):
    __tablename__ = "tag"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True)
    articles = relationship("Article", secondary="article_tag", back_populates="tags")

class Article(Base):
    __tablename__ = "article"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False, index=True)
    content = Column(Text, nullable=False)
    author_id = Column(Integer, ForeignKey('users.id'))
    author = relationship("User", back_populates="articles")
    tags = relationship("Tag", secondary="article_tag", back_populates="articles", lazy="dynamic")
