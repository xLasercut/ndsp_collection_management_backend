from tables.schema import DataItemConstraint, DataItem

data_item_email = DataItem(
    data_item_id="email",
    data_item_type="string",
    display_name="Email"
)

data_item_email_regex_constraint = DataItemConstraint(
    data_item_constraint_id="email_regex",
    data_item_id="email",
    constraint_type="regex",
    constraint_value="\d+@.*\.com"
)
