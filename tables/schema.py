from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from tables.common import Base


class CollectionSpecification(Base):
    __tablename__ = 'collection_specification'

    specification_id: Mapped[str] = mapped_column(String(100), primary_key=True)
    collection_id: Mapped[str] = mapped_column(ForeignKey('collection.collection_id'))
    specification_name: Mapped[str] = mapped_column(String(100))


class CollectionSpecificationColumn(Base):
    __tablename__ = 'collection_specification_column'

    collection_specification_column_id: Mapped[str] = mapped_column(String(100), primary_key=True)
    specification_id: Mapped[str] = mapped_column(ForeignKey('collection_specification.specification_id'))
    column_name: Mapped[str] = mapped_column(String(100))
    data_item_id: Mapped[str] = mapped_column(String(100))
    mandatory: Mapped[bool]
    validation_failure_error_code: Mapped[str] = mapped_column(String(100))
    validation_failure_error_message: Mapped[str] = mapped_column(String(100))
    validation_failure_response: Mapped[str] = mapped_column(String(100))


class DataItem(Base):
    __tablename__ = 'data_item'

    data_item_id: Mapped[str] = mapped_column(String(100), primary_key=True)
    display_name: Mapped[str] = mapped_column(String(100))
    data_item_type: Mapped[str] = mapped_column(ForeignKey('data_item_type.data_item_type'))


class DataItemType(Base):
    __tablename__ = 'data_item_type'

    data_item_type: Mapped[str] = mapped_column(String(100), primary_key=True)
    display_name: Mapped[str] = mapped_column(String(100))


class DataItemAllowedConstraint(Base):
    __tablename__ = 'data_item_allowed_constraint'

    constraint_type: Mapped[str] = mapped_column(String(100), primary_key=True)
    data_item_type: Mapped[str] = mapped_column(ForeignKey('data_item_type.data_item_type'))
    display_name: Mapped[str] = mapped_column(String(100))

    UniqueConstraint('constraint_type', 'data_item_type')


class DataItemConstraint(Base):
    __tablename__ = 'data_item_constraint'

    data_item_id: Mapped[str] = mapped_column(ForeignKey('data_item.data_item_id'), primary_key=True)
    constraint_type: Mapped[str] = mapped_column(ForeignKey('data_item_allowed_constraint.constraint_type'))
    constraint_value: Mapped[str] = mapped_column(String(100))

    UniqueConstraint('data_item_id', 'constraint_type')
