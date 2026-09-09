from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from tables.common import Base

engine = create_engine('mysql+pymysql://root:example@localhost/ndsp', echo=True)

Base.metadata.create_all(engine)
