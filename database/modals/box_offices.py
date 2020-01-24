from database.database import create_table_database


def create_box_offices_table():
    query = """CREATE TABLE IF NOT EXISTS box_offices (
                        boxofficeId INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT)"""
    create_table_database(query)


create_box_offices_table()
