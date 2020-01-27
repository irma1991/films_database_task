from database.database import create_table_database


def create_studios_table():
    query = """CREATE TABLE IF NOT EXISTS studios (
                        studioId INTEGER PRIMARY KEY AUTOINCREMENT,
                        studioName TEXT"""

    create_table_database(query)


create_studios_table()
