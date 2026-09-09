from tables.data.data_item.data_item_types.date_type import date_data_item_type, date_data_item_format_constraint
from tables.data.data_item.data_item_types.string_type import string_data_item_type, string_data_item_length_constraint, \
    string_data_item_regrex_constraint
from tables.data.data_item.date_of_birth import data_item_date_of_birth, data_item_date_of_birth_format_constraint
from tables.data.data_item.name import data_item_name, data_item_name_constraint

data_item_types = [

    string_data_item_type,
    date_data_item_type
]

data_item_type_allowed_constraints = [
    # string
    string_data_item_length_constraint,
    string_data_item_regrex_constraint,
    # date
    date_data_item_format_constraint
]

data_items = [
    data_item_name,
    data_item_date_of_birth
]

data_item_constraints = [
    data_item_name_constraint,
    data_item_date_of_birth_format_constraint
]
