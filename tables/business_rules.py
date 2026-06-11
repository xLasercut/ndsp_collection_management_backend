from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class ComplexRule(DeclarativeBase):
    __tablename__ = 'complex_rule'

    complex_rule_id: Mapped[str] = mapped_column('complex_rule_id', primary_key=True)
    complex_rule_name: Mapped[str]
    complex_rule_expression: Mapped[str]


class ComplexRuleAvailableField(DeclarativeBase):
    __tablename__ = 'complex_rule_available_field'

    complex_rule_field_id: Mapped[str] = mapped_column('complex_rule_field_id', primary_key=True)
    complex_rule_id: Mapped[str] = mapped_column('complex_rule_id', primary_key=True)
    complex_rule_field_name: Mapped[str]
    complex_rule_field_type: Mapped[str]


class CollectionBusinessRule(DeclarativeBase):
    __tablename__ = 'collection_business_rule'

    collection_business_rule_id: Mapped[str] = mapped_column('collection_business_rule_id', primary_key=True)
    collection_id: Mapped[str] = mapped_column('collection_id')
    complex_rule_id: Mapped[str] = mapped_column('complex_rule_id')


class CollectionBusinessRuleField(DeclarativeBase):
    __tablename__ = 'collection_business_rule_field'

    pk: Mapped[str] = mapped_column('pk', primary_key=True)
    collection_business_rule_id: Mapped[str]
    complex_rule_field_id: Mapped[str]
    field_id: Mapped[str]
    field_value: Mapped[str]
