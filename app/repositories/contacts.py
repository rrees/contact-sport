from .connect import connect

from .sql import contacts as sql_contacts


def all():
    with connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql_contacts.all)
            return [row for row in cursor]


def create(name, tags=None):
    if not tags:
        tags = []

    with connect() as conn:
        with conn.cursor() as cursor:
            params = {"name": name, "tags": tags}
            cursor.execute(sql_contacts.insert, params)
            return cursor.fetchone().get("row")


def full(an_id):
    params = {"external_id": an_id}

    with connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql_contacts.full, params)
            return cursor.fetchone()


def directory_contacts(directory_external_id):
    params = {"directory_id": directory_external_id}

    with connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql_contacts.in_directory, params)

            return cursor.fetchall()


def by_name(name):
    params = {"name": f"%{name}%"}

    with connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql_contacts.find_by_name, params)

            return cursor.fetchall()
