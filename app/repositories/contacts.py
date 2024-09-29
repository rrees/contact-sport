import uuid

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
            params = {"name": name, "tags": tags, "external_id": uuid.uuid4()}
            cursor.execute(sql_contacts.insert, params)


def full(an_id):
    params = {"external_id": an_id}

    with connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql_contacts.full, params)
            return cursor.fetchone()
