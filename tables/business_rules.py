from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class BusinessRules(DeclarativeBase):
    __tablename__ = 'business_rules'

    business_rule_id: Mapped[str] = mapped_column('business_rule_id', primary_key=True)
    business_rule_name: Mapped[str]
    business_rule_expression: Mapped[str]


class BusinessRuleAvailableFields(DeclarativeBase):
    __tablename__ = 'business_rule_available_fields'

    business_rule_field_id: Mapped[str] = mapped_column('business_rule_field_id', primary_key=True)
    business_rule_id: Mapped[str] = mapped_column('business_rule_id', primary_key=True)
    business_rule_field_names: Mapped[list[str]]
    business_rule_field_type: Mapped[str]