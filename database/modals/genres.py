from database.database import create_table_database, query_database
from entities.genre import Genre


def create_genres_table():
    query = """CREATE TABLE IF NOT EXISTS genres (
                        genresId INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT)"""
    create_table_database(query)


def create_movies_genres_table():
    query = """CREATE TABLE IF NOT EXISTS movies_genres (
                        movies_genres_Id INTEGER PRIMARY KEY AUTOINCREMENT,  
                        genresId int,
                        moviesId int, 
                        FOREIGN KEY (genresId) REFERENCES genres(genresId),                  
                        FOREIGN KEY (moviesId) REFERENCES movies(moviesId))"""
    create_table_database(query)


create_genres_table()
create_movies_genres_table()

query_database("PRAGMA table_info(genres)")
query_database("PRAGMA table_info(movies_genres)")