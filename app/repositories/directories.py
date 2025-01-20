from .connect import connect
from .sql import directories as directories_sql


def all():
    with connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute(directories_sql.all)
            return cursor.fetchall()


def directory(directory_id):
    with connect() as conn:
        with conn.cursor() as cursor:
            params = {"directory_id": directory_id}
            cursor.execute(directories_sql.directory, params)

            return cursor.fetchone()


def create(directory_name):
    with connect() as conn:
        with conn.cursor() as cursor:
            params = {"name": directory_name}
            cursor.execute(directories_sql.insert, params)

            return cursor.fetchone().get("row")
