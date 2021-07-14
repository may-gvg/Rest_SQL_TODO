from ex_01_conection_to_db import create_connection

from ex_04_selecty import *

conn = create_connection("database.db")

# wszystkie projekty

select_all(conn, "projects")


# wszystkie zadania

select_all(conn, "tasks")

# wszystkie zadania dla projektu o id 1

select_where(conn, "tasks", projekt_id=1)

# wszystkie zadania ze statusem ended

select_where(conn, "tasks", status="ended")



def delete_where(conn, table, **kwargs):
    """
   Delete from table where attributes from
   :param conn:  Connection to the SQLite database
   :param table: table name
   :param kwargs: dict of attributes and values
   :return:
   """
    qs = []
    values = tuple()
    for k, v in kwargs.items():
        qs.append(f"{k}=?")
        values += (v,)
    q = " AND ".join(qs)

    sql = f'DELETE FROM {table} WHERE {q}'
    cur = conn.cursor()
    cur.execute(sql, values)
    conn.commit()
    print("Deleted")


def delete_all(conn, table):
    """
   Delete all rows from table
   :param conn: Connection to the SQLite database
   :param table: table name
   :return:
   """
    sql = f'DELETE FROM {table}'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    print("Deleted")


if __name__ == "__main__":
    conn = create_connection("database.db")
    delete_where(conn, "tasks", id=2)
    delete_all(conn, "tasks")
