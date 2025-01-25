all = """SELECT
    external_id,
    name,
    tags
FROM contact
ORDER BY name"""

insert = """
INSERT INTO contact (
    name,
    tags
) VALUES (
    %(name)s,
    %(tags)s
) RETURNING (id, external_id)"""


full = """
SELECT
    external_id,
    name,
    tags,
    ARRAY(
        SELECT
            ARRAY[
                external_id::text,
                label,
                address
            ]
        FROM address
        WHERE contact_id = contact.id
    ) AS addresses,
    ARRAY (
        SELECT
            ARRAY[
                external_id::text,
                label,
                email
            ]
            FROM email
            WHERE contact_id = contact.id
    ) AS emails
FROM contact
WHERE external_id = %(external_id)s"""


in_directory = """
SELECT *
FROM contact
WHERE id IN (
    SELECT contact_id
    FROM directory_entries
    WHERE directory_id = (
        SELECT id
        FROM directories
        WHERE external_id = %(directory_id)s
    )
)"""

find_by_name = """
SELECT *
FROM contact
WHERE name ILIKE %(name)s
"""
