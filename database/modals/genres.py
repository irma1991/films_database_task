from database.database import create_table_database


def create_genres_table():
    query = """CREATE TABLE IF NOT EXISTS genres (
                        genresId INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT)"""
    create_table_database(query)


create_genres_table()

def create_genres_movies_table():
    query = """CREATE TABLE IF NOT EXISTS genres_movies (
                        genres_movies_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        genresId INTEGER,
                        moviesId INTEGER,
                        FOREIGN KEY (genresId) REFERENCES genres(genresId),
                        FOREIGN KEY (moviesId) REFERENCES movies(moviesId))"""
    create_table_database(query)


create_genres_movies_table()
