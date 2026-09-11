from tables.complex_rules import ComplexRule

greater_than = ComplexRule(
    complex_rule_id="greater_than",
    display_name="Greater than",
    expression="column0 > column1",
    number_of_columns=2
)