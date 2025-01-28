all = """
SELECT *
FROM directories
"""

directory = """
SELECT *
FROM directories
WHERE external_id = %(directory_id)s
"""

insert = """
INSERT INTO directories (
    name
) VALUES (
    %(name)s
) RETURNING (id, external_id)"""


add_contact = """
INSERT INTO directory_entries (
    directory_id,
    contact_id
) VALUES (
(SELECT id FROM directories WHERE external_id = %(directory_id)s),
(SELECT id FROM contact WHERE external_id = %(contact_id)s) 
)
ON CONFLICT DO NOTHING
"""
