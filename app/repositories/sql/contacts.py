all = """SELECT
    external_id,
    name,
    tags
FROM contact
ORDER BY name"""

insert = """
INSERT INTO contact (
    name,
    tags,
    external_id
) VALUES (
    %(name)s,
    %(tags)s,
    %(external_id)s
) RETURNING (id, external_id)"""
