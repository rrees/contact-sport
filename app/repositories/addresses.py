import uuid

from .connect import connect
from .sql import addresses as addresses_sql


def create(contact_external_id, label, address):
    external_id = uuid.uuid4()

    params = {
        "label": label,
        "address": address,
        "external_id": external_id,
    }

    with connect() as conn:
        with conn.cursor() as cursor:
            params = {
                "contact_id": contact_external_id,
                "external_id": uuid.uuid4(),
                "label": label,
                "address": address,
            }
            cursor.execute(addresses_sql.insert, params)

            return cursor.fetchone()
