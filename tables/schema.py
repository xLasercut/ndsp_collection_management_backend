from sqlalchemy import UniqueConstraint

from sqlmodel import SQLModel, Field


class CollectionSpecification(SQLModel, table=True):
    __tablename__ = 'collection_specification'

    specification_id: str = Field(primary_key=True)
    collection_id: str
    specification_name: str


class CollectionSpecificationColumn(SQLModel, table=True):
    __tablename__ = 'data_item_column_specification'

    collection_specification_column_id: str = Field(primary_key=True)
    specification_id: str = Field(foreign_key='collection_specification.specification_id')
    column_name: str
    data_item_id: str
    mandatory: bool
    validation_failure_error_code: str
    validation_failure_error_message: str
    validation_failure_response: str


class DataItem(SQLModel, table=True):
    __tablename__ = 'data_item'

    data_item_id: str = Field(primary_key=True)
    display_name: str
    data_item_type: str = Field(foreign_key='data_item_type.data_item_type')


class DataItemType(SQLModel, table=True):
    __tablename__ = 'data_item_type'

    data_item_type: str = Field(primary_key=True)
    display_name: str


class DataItemAllowedConstraint(SQLModel, table=True):
    __tablename__ = 'data_item_allowed_constraint'

    constraint_type: str = Field(primary_key=True)
    data_item_type: str = Field(foreign_key='data_item_type.data_item_type')
    display_name: str

    UniqueConstraint('constraint_type', 'data_item_type')


class DataItemConstraint(SQLModel, table=True):
    __tablename__ = 'data_item_constraint'

    data_item_constraint_id: str = Field(primary_key=True)
    data_item_id: str = Field(foreign_key='data_item.data_item_id')
    constraint_type: str = Field(foreign_key='data_item_allowed_constraint.constraint_type')
    constraint_value: str

    UniqueConstraint('data_item_id', 'constraint_type')
