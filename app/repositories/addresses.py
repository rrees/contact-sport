from .connect import connect
from .sql import addresses as addresses_sql


def create(contact_external_id, label, address):
    with connect() as conn:
        with conn.cursor() as cursor:
            params = {
                "contact_id": contact_external_id,
                "label": label,
                "address": address,
            }

            cursor.execute(addresses_sql.insert, params)

            result = cursor.fetchone()

            return result["row"]
