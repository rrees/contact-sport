from .connect import connect
from .sql import emails as emails_sql


def create(contact_external_id, label, email):
    with connect() as conn:
        with conn.cursor() as cursor:
            params = {
                "contact_id": contact_external_id,
                "label": label,
                "email": email,
            }

            cursor.execute(emails_sql.insert, params)

            result = cursor.fetchone()

            return result["row"]
