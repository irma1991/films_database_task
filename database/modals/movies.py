from database.database import create_table_database, query_database

from database.database import create_table_database, query_database
from entities.movie import Movie

def create_movies_table():
    query = """CREATE TABLE IF NOT EXISTS movies (
                        moviesId INTEGER PRIMARY KEY AUTOINCREMENT,
                        movie_name TEXT,
                        release_date DATE,
                        rating REAL,
                        genre TEXT,
                        studioId INTEGER,
                        boxOfficeId INTEGER,
                        FOREIGN KEY(studioId) REFERENCES studios(studioId),
                        FOREIGN KEY(boxOfficeId) REFERENCES box_offices(boxOfficeId))"""

def insert_into_movies_table(movies):  # funkcija laukianti parametro
    query = """INSERT INTO movies (moviesId, movie_name, release_date, rating, genre, studioId, boxofficeId ) 
                      VALUES(?, ?, ?, ?, ?, ?, ?)"""
    params = (movies.moviesId, movies.movie_name, movies.release_date, movies.rating, movies.genre, movies.studioId, movies.boxofficeId)  # paduodu funkcijos laukiamo parametro reiksmes
    query_database(query, params)


def get_movies_table():
    query = "SELECT * FROM movies"
    query_database(query)


def update_movies_table(movies):
    query = "UPDATE movies SET movie_name = ? WHERE moviesId = ?"
    params = (movies.movie_name, movies.moviesId)
    query_database(query, params)

def delete_movies_table(moviesId):
    query = "DELETE FROM movies WHERE moviesId = ?"
    params = (moviesId, ) #python tuple, jei be skliaustu ir kablelio, butu  variable
    query_database(query, params)

# query_database("PRAGMA table_info(movies)")
create_movies_table()
# create_table_database("DROP TABLE movies")
movies1 = Movie(None, "pirmas", 2019, 2.7, "Zanras", 2, 1)
movies2 = Movie(None, "antras filmas", 2018, 9.2, "Zanras", 1, 2)
# insert_into_movies_table(movies2)
movies3 = Movie(2, "update Test", 2018, 9.2, "Zanras", 1, 2)
update_movies_table(movies3)
get_movies_table()
