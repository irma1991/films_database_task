from database.database import create_table_database


def create_box_offices_table():
    query = """CREATE TABLE IF NOT EXISTS box_offices (
                        boxOfficeId INTEGER PRIMARY KEY AUTOINCREMENT,
                        gross REAL"""

    create_table_database(query)


create_box_offices_table()
