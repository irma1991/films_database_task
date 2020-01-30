from database.database import create_table_database
from entities.genre import Genre


def create_genres_table():
    query = """CREATE TABLE IF NOT EXISTS genres (
                        genresId INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT)"""
    create_table_database(query)


def create_genres_movies_table():
    query = """CREATE TABLE IF NOT EXISTS genres_movies (
                        genres_movies_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        genresId INTEGER,
                        moviesId INTEGER,
                        FOREIGN KEY (genresId) REFERENCES genres(genresId),
                        FOREIGN KEY (moviesId) REFERENCES movies(moviesId))"""
    create_table_database(query)

create_genres_table()
create_genres_movies_table()

query_database("PRAGMA table_info(genres)")
query_database("PRAGMA table_info(genres_movies)")
