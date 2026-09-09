from tables.schema import DataItemAllowedConstraint, DataItemType

string_data_item_type = DataItemType(
    data_item_type="string",
    display_name="String",
)

string_data_item_length_constraint = DataItemAllowedConstraint(
    data_item_type="string",
    display_name="String Length",
    constraint_type="length"
)

string_data_item_regrex_constraint = DataItemAllowedConstraint(
    data_item_type="string",
    display_name="Regular Expression",
    constraint_type="regex"
)