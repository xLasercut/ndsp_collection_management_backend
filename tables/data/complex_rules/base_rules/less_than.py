from tables.complex_rules import ComplexRule

less_than = ComplexRule(
    complex_rule_id="less_than",
    display_name="Less than",
    expression="column0 < column1",
    number_of_columns=2
)