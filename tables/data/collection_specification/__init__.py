from tables.data.collection_specification.user import user, user_details_column, user_email_column
from tables.data.collection_specification.user_details import user_detail, user_detail_name_column, \
    user_detail_dob_column

collection_specifications = [
    [
        user,
        user_detail
    ],
    [
        user_details_column,
        user_email_column,
        user_detail_name_column,
        user_detail_dob_column
    ]
]
