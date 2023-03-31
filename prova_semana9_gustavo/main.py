from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from src.models.base import Base
engine = create_engine("sqlite+pysqlite:///data.db", echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)
