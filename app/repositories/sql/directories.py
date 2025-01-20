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
