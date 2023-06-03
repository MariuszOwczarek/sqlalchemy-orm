from sqlalchemy import Integer, Column, String, DateTime, Float, Text ,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from session import engine
from datetime import datetime

Base = declarative_base(bind=engine)


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    login = Column(String(50), unique=True, nullable=False)
    salary = Column(Float, default=0)
    email = Column(String(50), unique=True, nullable=False)
    registration_date = Column(DateTime, default=datetime.now)
    articles = relationship("Article")

    def __repr__(self):
        return f'Author({self.login})'

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), unique=True, nullable=False)
    content = Column(Text(1000), nullable=False)
    publication_date = Column(DateTime, default=datetime.now)
    author_id = Column(Integer, ForeignKey("authors.id"))

    def __str__(self):
        return f"Article({self.title})"

