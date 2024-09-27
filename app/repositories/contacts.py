from .connect import connect

from .sql import contacts as sql_contacts


def all():
    with connect() as conn:
        with conn.cursor() as cursor:
            return [row for row in cursor.execute(sql_contacts.all)]
