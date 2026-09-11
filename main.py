from sqlmodel import create_engine, Session

from tables.data.collection import collections
from tables.data.collection_specification import collection_specifications
from tables.data.complex_rules import base_rules, complex_rules, complex_rule_columns
from tables.data.data_item import data_item_types, data_items, data_item_type_allowed_constraints, \
    data_item_constraints
from tables.functions import create_tables, drop_tables

engine = create_engine('mysql+pymysql://root:example@localhost/ndsp', echo=True)

drop_tables(engine)
create_tables(engine)


def generate_test_data(session: Session):
    session.add_all(data_item_types)
    session.commit()

    session.add_all(data_item_type_allowed_constraints)
    session.commit()

    session.add_all(data_items)
    session.commit()

    session.add_all(data_item_constraints)
    session.commit()

    session.add_all(collections)
    session.commit()

    session.add_all(base_rules)
    session.commit()

    for items in collection_specifications:
        session.add_all(items)
        session.commit()

    session.add_all(complex_rules)
    session.commit()

    session.add_all(complex_rule_columns)
    session.commit()


with Session(engine) as session:
    generate_test_data(session)
