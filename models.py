from sqlalchemy import Integer, Column, String, DateTime, Float, Text, ForeignKey, Table
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
    articles = relationship("Article", back_populates="author")

    def __repr__(self):
        return f'Author({self.login})'

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), unique=True, nullable=False)
    content = Column(Text, nullable=False)
    publication_date = Column(DateTime, default=datetime.now)
    author_id = Column(Integer, ForeignKey("authors.id"))
    author = relationship("Author", back_populates='articles')
    hashtags = relationship("Hashtags", secondary="articles_hashtags",back_populates='articles')

    def __str__(self):
        return f"Article({self.title})"


class Hashtags(Base):
    __tablename__ = "hashtags"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)
    creation_date = Column(DateTime, default=datetime.now)
    articles = relationship("Article", secondary="articles_hashtags",back_populates='hashtags')

    def __str__(self):
        return f'Hashtags({self.name})'


# tworzenie tabel w inny sposob za pomoca Table a nie Class
article_hashtag = Table(
    "articles_hashtags",
    Base.metadata,
    Column("article_id", Integer, ForeignKey("articles.id"), primary_key=True),
    Column("hashtag_id", Integer, ForeignKey("hashtags.id"), primary_key=True)
)
