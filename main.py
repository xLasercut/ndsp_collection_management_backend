from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from tables.collection import Collection
from tables.schema import CollectionSpecification, CollectionSpecificationColumn, DataItem, DataItemType, DataItemAllowedConstraint, DataItemConstraint

engine = create_engine('mysql+pymysql://root:example@localhost/ndsp', echo=True)

tables = [
    Collection,
    DataItemType,
    CollectionSpecification,
    CollectionSpecificationColumn,
    DataItem,
    DataItemAllowedConstraint,
    DataItemConstraint,
]

for table in tables:
    table.metadata.create_all(engine)