from tables.complex_rules import ComplexRule

or_rule = ComplexRule(
    complex_rule_id="or",
    display_name="Or",
    expression="column0 | column1",
    number_of_columns=2
)