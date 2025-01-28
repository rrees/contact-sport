from .connect import connect
from .sql import directories as directories_sql


def all():
    with connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute(directories_sql.all)
            return cursor.fetchall()


def directory(directory_id):
    params = {"directory_id": directory_id}

    with connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute(directories_sql.directory, params)

            return cursor.fetchone()


def create(directory_name):
    params = {"name": directory_name}

    with connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute(directories_sql.insert, params)

            return cursor.fetchone().get("row")


def add_contact(directory_id, contact_id):
    params = {"directory_id": directory_id, "contact_id": contact_id}

    with connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute(directories_sql.add_contact, params)
            return directory_id
