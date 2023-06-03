from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#engine = create_engine("mysql+pymysql://root:prodigy1#@localhost:3306/blog")  #my sql
engine = create_engine("postgresql://postgres:prodigy1#@localhost:5432/blog")  #my postgres
Session = sessionmaker(bind=engine)
session = Session()


def commit_on_success(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        session.commit()
        return result
    return wrapper