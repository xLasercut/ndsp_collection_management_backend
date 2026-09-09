from tables.schema import DataItemConstraint, DataItem

data_item_name = DataItem(
    data_item_id="name",
    data_item_type="string",
    display_name="Name"
)

data_item_name_constraint = DataItemConstraint(
    data_item_id="name",
    constraint_type="length",
    constraint_value="10"
)
