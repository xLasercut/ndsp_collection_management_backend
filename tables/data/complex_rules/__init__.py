from tables.data.complex_rules.base_rules.and_rule import and_rule
from tables.data.complex_rules.base_rules.equal import equal_rule
from tables.data.complex_rules.base_rules.greater_than import greater_than
from tables.data.complex_rules.base_rules.less_than import less_than
from tables.data.complex_rules.base_rules.or_rule import or_rule
from tables.data.complex_rules.name_is_john_and_dob_greater_than import name_is_john_rule, name_is_john_rule_column0, \
    name_is_john_rule_column1, dob_is_greater_than_rule, dob_is_greater_than_rule_column0, \
    dob_is_greater_than_rule_column1, name_is_john_and_dob_greater_than_rule, name_is_john_and_dob_greater_than_column0, \
    name_is_john_and_dob_greater_than_column1

base_rules = [
    and_rule,
    equal_rule,
    or_rule,
    greater_than,
    less_than,
]

complex_rules = [
    name_is_john_rule,
    dob_is_greater_than_rule,
    name_is_john_and_dob_greater_than_rule,
]

complex_rule_columns = [
    name_is_john_rule_column0,
    name_is_john_rule_column1,
    dob_is_greater_than_rule_column0,
    dob_is_greater_than_rule_column1,
    name_is_john_and_dob_greater_than_column0,
    name_is_john_and_dob_greater_than_column1
]
