from tables.schema import CollectionSpecification, CollectionSpecificationColumn

user = CollectionSpecification(
    specification_id="user",
    collection_id="test_collection",
    specification_name="user",
)

user_details_column = CollectionSpecificationColumn(
    collection_specification_column_id="user_column_details",
    specification_id="user",
    column_name="details",
    data_item_id="user_details",
    mandatory=True,
    validation_failure_error_code="E001",
    validation_failure_error_message="User details invalid",
    validation_failure_response="reject"
)

user_email_column = CollectionSpecificationColumn(
    collection_specification_column_id="user_column_email",
    specification_id="user",
    column_name="email",
    data_item_id="email",
    mandatory=True,
    validation_failure_error_code="E002",
    validation_failure_error_message="email invalid",
    validation_failure_response="warning"
)