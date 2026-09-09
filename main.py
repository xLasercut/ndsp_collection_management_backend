from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from tables.data.collection import collections
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


with Session(engine) as session:
    generate_test_data(session)
