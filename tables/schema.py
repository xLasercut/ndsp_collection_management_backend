from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from tables.common import Base


class CollectionSpecification(Base):
    __tablename__ = 'collection_specification'

    specification_id: Mapped[str] = mapped_column('specification_id', primary_key=True)
    collection_id: Mapped[str] = mapped_column(ForeignKey('collection.collection_id'), primary_key=True)
    specification_name: Mapped[str]
    reporting_fields: Mapped[str]


class CollectionSpecificationColumn(Base):
    __tablename__ = 'collection_specification_column'

    collection_specification_column_id: Mapped[str] = mapped_column('collection_specification_column_id',
                                                                    primary_key=True)
    specification_id: Mapped[str] = mapped_column(ForeignKey('collection_specification.specification_id'))
    column_name: Mapped[str]
    data_item_id: Mapped[str]
    mandatory: Mapped[bool]
    validation_failure_error_code: Mapped[str]
    validation_failure_error_message: Mapped[str]
    validation_failure_response: Mapped[str]


class DataItem(Base):
    __tablename__ = 'data_item'

    data_item_id: Mapped[str] = mapped_column('data_item_id', primary_key=True)
    display_name: Mapped[str]
    data_item_type: Mapped[str] = mapped_column(ForeignKey('data_item_type.data_item_type'), primary_key=True)


class DataItemType(Base):
    __tablename__ = 'data_item_type'

    data_item_type: Mapped[str] = mapped_column('data_item_type', primary_key=True)
    display_name: Mapped[str]


class DataItemAllowedConstraint(Base):
    __tablename__ = 'data_item_allowed_constraint'

    constraint_type: Mapped[str] = mapped_column('constraint_type', primary_key=True)
    data_item_type: Mapped[str] = mapped_column(ForeignKey('data_item_type.data_item_type'), primary_key=True)
    display_name: Mapped[str]


class DataItemConstraint(Base):
    __tablename__ = 'data_item_constraint'

    data_item_type: Mapped[str] = mapped_column('data_item_type.data_item_type', primary_key=True)
    data_item_id: Mapped[str] = mapped_column(ForeignKey('data_item.data_item_id'), primary_key=True)
    constraint_type: Mapped[str] = mapped_column(ForeignKey('data_item_allowed_constraint.constraint_type'), primary_key=True)
    constraint_value: Mapped[str]
