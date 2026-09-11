from typing import Optional

from sqlmodel import SQLModel, Field


class ComplexRule(SQLModel, table=True):
    __tablename__ = 'complex_rule'

    complex_rule_id: str = Field(primary_key=True)
    display_name: str
    expression: str
    number_of_columns: int


class CollectionComplexRule(SQLModel, table=True):
    __tablename__ = 'collection_complex_rule'

    collection_rule_id: str = Field(primary_key=True)
    complex_rule_id: str = Field(foreign_key='complex_rule.complex_rule_id')
    collection_id: str


class CollectionComplexRuleColumn(SQLModel, table=True):
    __tablename__ = 'collection_complex_rule_column'

    pk: str = Field(primary_key=True)
    collection_rule_id: str = Field(foreign_key='collection_complex_rule.collection_rule_id')
    column_id: Optional[str]
    static_value: Optional[str]
    column_order: str
