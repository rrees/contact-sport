from .connect import connect
from .sql import directories as directories_sql


def all():
    with connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute(directories_sql.all)
            return cursor.fetchall()
