insert = """INSERT INTO email (
    contact_id,
    label,
    email
) VALUES (
    (SELECT id FROM contact WHERE external_id = %(contact_id)s),
    %(label)s,
    %(email)s
)
RETURNING (id, external_id)"""
