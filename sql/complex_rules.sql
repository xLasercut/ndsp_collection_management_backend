SELECT *
FROM (SELECT collection_rule_id,
             JSON_OBJECTAGG(column_order, column_substitution) as column_substitution,
             GROUP_CONCAT(DISTINCT complex_rule_id)            as complex_rule_id
      FROM (SELECT *
            FROM (SELECT pk,
                         collection_rule_id,
                         column_id,
                         static_value,
                         column_order,
                         complex_rule_id,
                         collection_id,
                         concat(specification_id, '.', column_name) as column_substitution
                  FROM (SELECT pk,
                               collection_complex_rule.collection_rule_id,
                               column_id,
                               static_value,
                               column_order,
                               complex_rule_id,
                               collection_id
                        FROM collection_complex_rule_column
                                 JOIN collection_complex_rule
                                      ON collection_complex_rule_column.collection_rule_id =
                                         collection_complex_rule.collection_rule_id) AS collection_rules_with_columns
                           JOIN data_item_column_specification
                                ON data_item_column_specification.collection_specification_column_id =
                                   column_id) as rule_with_columns
            UNION
            (SELECT pk,
                    collection_complex_rule.collection_rule_id,
                    column_id,
                    static_value,
                    column_order,
                    complex_rule_id,
                    collection_id,
                    concat('"', static_value, '"') as column_substitution
             FROM collection_complex_rule_column
                      JOIN collection_complex_rule
                           ON collection_complex_rule_column.collection_rule_id =
                              collection_complex_rule.collection_rule_id
             WHERE static_value is not null)
            UNION
            (SELECT pk,
                    collection_complex_rule.collection_rule_id,
                    column_id,
                    static_value,
                    column_order,
                    complex_rule_id,
                    collection_id,
                    column_substitution
             FROM (SELECT pk,
                          collection_complex_rule_column.collection_rule_id,
                          column_id,
                          static_value,
                          column_order,
                          column_id as column_substitution
                   FROM collection_complex_rule_column
                            JOIN collection_complex_rule
                                 ON collection_complex_rule_column.column_id =
                                    collection_complex_rule.collection_rule_id) as nested_rules
                      JOIN collection_complex_rule
                           ON collection_complex_rule.collection_rule_id =
                              nested_rules.collection_rule_id)) AS all_rules
      GROUP BY collection_rule_id) as all_rules_grouped
         JOIN complex_rule
              ON all_rules_grouped.complex_rule_id = complex_rule.complex_rule_id