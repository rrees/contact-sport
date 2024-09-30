insert = """INSERT INTO address (
    external_id,
    contact_id,
    label,
    address
) VALUES (
    %(external_id)s,
    (SELECT id FROM contact WHERE external_id = %(contact_id)s),
    %(label)s,
    %(address)s
)
RETURNING (id, external_id)"""
