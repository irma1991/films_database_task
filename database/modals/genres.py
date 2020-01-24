from database.database import create_table_database


def create_genres_table():
    query = """CREATE TABLE IF NOT EXISTS genres (
                        genresId INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT)"""
    create_table_database(query)


create_genres_table()
