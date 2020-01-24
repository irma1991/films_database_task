from database.database import create_table_database


def create_directors_table():
    query = """CREATE TABLE IF NOT EXISTS directors (
                        directorsId INTEGER PRIMARY KEY AUTOINCREMENT,
                        Name TEXT)"""
    create_table_database(query)


create_directors_table()
