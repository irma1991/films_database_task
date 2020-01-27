from database.database import create_table_database


def create_directors_table():
    query = """CREATE TABLE IF NOT EXISTS directors (
                        directorsId INTEGER PRIMARY KEY AUTOINCREMENT,
                        Name TEXT)"""
    create_table_database(query)


create_directors_table()

def create_directors_movies_table():
    query = """CREATE TABLE IF NOT EXISTS directors_movies (
                        directors_movies_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        directorsId INTEGER,
                        moviesId INTEGER,
                        FOREIGN KEY (directorsId) REFERENCES directors(directorsId),
                        FOREIGN KEY (moviesId) REFERENCES movies(moviesId))"""
    create_table_database(query)


create_directors_movies_table()
