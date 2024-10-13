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
