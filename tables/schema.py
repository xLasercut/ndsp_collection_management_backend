from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class CollectionDataset(DeclarativeBase):
    __tablename__ = 'collection_dataset'

    dataset_id: Mapped[str] = mapped_column('dataset_id', primary_key=True)
    collection_id: Mapped[str] = mapped_column(ForeignKey('collection.collection_id'), primary_key=True)
    schema_id: Mapped[str] = mapped_column(ForeignKey('schema.schema_id'))
    dataset_name: Mapped[str]
    reporting_fields: Mapped[str]


class CollectionSchema(DeclarativeBase):
    __tablename__ = 'collection_schema'

    schema_id: Mapped[str] = mapped_column('schema_id', primary_key=True)
    collection_id: Mapped[str] = mapped_column(ForeignKey('collection.collection_id'), primary_key=True)
    schema_name: Mapped[str]


class SchemaField(DeclarativeBase):
    __tablename__ = 'schema_field'

    field_id: Mapped[str] = mapped_column('field_id', primary_key=True)
    schema_id: Mapped[str] = mapped_column(ForeignKey('schema.schema_id'))
    schema_field_name: Mapped[str]
    data_item_id: Mapped[str]
    mandatory: Mapped[bool]
    validation_failure_error_code: Mapped[str]
    validation_failure_error_message: Mapped[str]
    validation_failure_response: Mapped[str]


class DataItem(DeclarativeBase):
    __tablename__ = 'data_item'

    data_item_id: Mapped[str] = mapped_column('data_item_id', primary_key=True)
    data_item_name: Mapped[str]
    data_item_base_type: Mapped[str]


class DataItemAvailableConstraint(DeclarativeBase):
    __tablename__ = 'data_item_available_constraint'

    data_item_constraint_id: Mapped[str] = mapped_column(ForeignKey('data_item_constraint.data_item_constraint_id'), primary_key=True)
    data_item_id: Mapped[str] = mapped_column(ForeignKey('data_item.data_item_id'), primary_key=True)

class DataItemConstraint(DeclarativeBase):
    __tablename__ = 'data_item_constraint'

    data_item_constraint_id: Mapped[str] = mapped_column('data_item_constraint_id', primary_key=True)
    data_item_constraint_type: Mapped[str]
    constraint_default_value: Mapped[str]
    constraint_name: Mapped[str]

class SchemaFieldConstraintValue(DeclarativeBase):
    __tablename__ = 'schema_field_constraint_value'

    pk: Mapped[str] = mapped_column('pk', primary_key=True)
    data_item_id: Mapped[str] = mapped_column(ForeignKey('data_item.data_item_id'), primary_key=True)
    data_item_constraint_id: Mapped[str] = mapped_column(ForeignKey('data_item_constraint.data_item_constraint_id'),
                                                         primary_key=True)
    constraint_value: Mapped[str]