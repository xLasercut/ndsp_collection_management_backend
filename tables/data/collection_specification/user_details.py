from tables.schema import CollectionSpecification, CollectionSpecificationColumn

user_detail = CollectionSpecification(
    specification_id="user_detail",
    collection_id="test_collection",
    specification_name="user details",
)

user_detail_name_column = CollectionSpecificationColumn(
    collection_specification_column_id="user_detail_column_name",
    specification_id="user_detail",
    column_name="name",
    data_item_id="name",
    mandatory=True,
    validation_failure_error_code="E003",
    validation_failure_error_message="User name invalid",
    validation_failure_response="reject"
)

user_detail_dob_column = CollectionSpecificationColumn(
    collection_specification_column_id="user_detail_column_dob",
    specification_id="user_detail",
    column_name="date_of_birth",
    data_item_id="date_of_birth",
    mandatory=True,
    validation_failure_error_code="E004",
    validation_failure_error_message="dob invalid",
    validation_failure_response="reject"
)
