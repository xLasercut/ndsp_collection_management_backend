from tables.schema import DataItemConstraint, DataItem

data_item_date_of_birth = DataItem(
    data_item_id="date_of_birth",
    data_item_type="date",
    display_name="Date of Birth"
)

data_item_date_of_birth_format_constraint = DataItemConstraint(
    data_item_id="date_of_birth",
    constraint_type="format",
    constraint_value="%y-%m-%d"
)
