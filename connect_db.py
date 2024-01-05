from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///D:/web_db/db1.db")
Session = sessionmaker(bind=engine)
session = Session()