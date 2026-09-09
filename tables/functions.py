from sqlalchemy import Engine
from tables.collection import Collection
from tables.schema import CollectionSpecification, CollectionSpecificationColumn, DataItem, DataItemType, DataItemAllowedConstraint, DataItemConstraint

tables = [
        Collection,
        DataItemType,
        CollectionSpecification,
        CollectionSpecificationColumn,
        DataItem,
        DataItemAllowedConstraint,
        DataItemConstraint,
    ]

def create_tables(engine: Engine):
    for table in tables:
        table.metadata.create_all(engine)


def drop_tables(engine: Engine):
    for table in tables:
        table.metadata.drop_all(engine)