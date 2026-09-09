from tables.schema import DataItemAllowedConstraint, DataItemType

date_data_item_type = DataItemType(
    data_item_type="date",
    display_name="Date",
)

date_data_item_format_constraint = DataItemAllowedConstraint(
    data_item_type="date",
    display_name="Date Formate",
    constraint_type="format"
)

