from tables.complex_rules import CollectionComplexRule, CollectionComplexRuleColumn

name_is_john_rule = CollectionComplexRule(
    collection_rule_id="name_is_john",
    complex_rule_id="equal",
    collection_id="test_collection"
)


name_is_john_rule_column0 = CollectionComplexRuleColumn(
    pk="name_is_john_rule_column0",
    column_id="user_detail_column_name",
    collection_rule_id="name_is_john",
    static_value=None,
    column_order="column0"
)

name_is_john_rule_column1 = CollectionComplexRuleColumn(
    pk="name_is_john_rule_column1",
    column_id=None,
    collection_rule_id="name_is_john",
    static_value="John",
    column_order="column1"
)

dob_is_greater_than_rule = CollectionComplexRule(
    collection_rule_id="dob_is_greater_than",
    complex_rule_id="greater_than",
    collection_id="test_collection"
)

dob_is_greater_than_rule_column0 = CollectionComplexRuleColumn(
    pk="dob_is_greater_than_rule_column0",
    column_id="user_detail_column_dob",
    collection_rule_id="dob_is_greater_than",
    static_value=None,
    column_order="column0"
)

dob_is_greater_than_rule_column1 = CollectionComplexRuleColumn(
    pk="dob_is_greater_than_rule_column1",
    column_id=None,
    collection_rule_id="dob_is_greater_than",
    static_value="2000-01-01",
    column_order="column1"
)


name_is_john_and_dob_greater_than_rule = CollectionComplexRule(
    collection_rule_id="name_is_john_and_dob_greater_than",
    complex_rule_id="and",
    collection_id="test_collection"
)

name_is_john_and_dob_greater_than_column0 = CollectionComplexRuleColumn(
    pk="name_is_john_and_dob_greater_than_column0",
    column_id="name_is_john",
    collection_rule_id="name_is_john_and_dob_greater_than",
    static_value=None,
    column_order="column0"
)

name_is_john_and_dob_greater_than_column1 = CollectionComplexRuleColumn(
    pk="name_is_john_and_dob_greater_than_column1",
    column_id="dob_is_greater_than",
    collection_rule_id="name_is_john_and_dob_greater_than",
    static_value=None,
    column_order="column1"
)