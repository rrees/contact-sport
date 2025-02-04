insert = """INSERT INTO address (
    contact_id,
    label,
    address
) VALUES (
    (SELECT id FROM contact WHERE external_id = %(contact_id)s),
    %(label)s,
    %(address)s
)
RETURNING (id, external_id)"""
