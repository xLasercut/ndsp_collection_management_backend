SELECT specification_id,
       JSON_OBJECTAGG(
               column_name,
               JSON_OBJECT(
                       schema_type,
                       data_item_type,
                       'constraints',
                       constraints
               )
       ) as fields
FROM (SELECT *
      FROM (SELECT *
            FROM (SELECT data_item.data_item_id,
                         display_name,
                         data_item_type,
                         JSON_OBJECTAGG(
                                 constraint_type,
                                 constraint_value
                         )          AS constraints,
                         'callable' AS schema_type
                  FROM data_item
                           Join data_item_constraint
                  WHERE data_item.data_item_id = data_item_constraint.data_item_id
                  GROUP BY data_item.data_item_id) AS data_items_with_constraints
                     JOIN data_item_column_specification
                          USING (data_item_id)) AS columns_with_data_items
      UNION
      (SELECT ''            as data_item_id,
              ''            as display_name,
              data_item_id  as data_item_type,
              JSON_OBJECT() as constraints,
              'model'       AS schema_type,
              collection_specification_column_id,
              data_item_column_specification.specification_id,
              column_name,
              mandatory,
              validation_failure_error_code,
              validation_failure_error_message,
              validation_failure_response
       FROM collection_specification
              JOIN data_item_column_specification
       ON data_item_column_specification.data_item_id = collection_specification.specification_id)) AS all_specs
GROUP BY specification_id