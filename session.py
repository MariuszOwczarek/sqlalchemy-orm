from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:prodigy1#@localhost:3306/blog")
Session = sessionmaker(bind=engine)
session = Session()