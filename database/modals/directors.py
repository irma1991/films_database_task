from database.database import create_table_database
from entities.director import Director


def create_directors_table():
    query = """CREATE TABLE IF NOT EXISTS directors (
                        directorsId INTEGER PRIMARY KEY AUTOINCREMENT,
                        Name TEXT)"""
    create_table_database(query)


def create_directors_movies_table():
    query = """CREATE TABLE IF NOT EXISTS directors_movies (
                        directors_movies_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        directorsId INTEGER,
                        moviesId INTEGER,
                        FOREIGN KEY (directorsId) REFERENCES directors(directorsId),
                        FOREIGN KEY (moviesId) REFERENCES movies(moviesId))"""
    create_table_database(query)

def insert_into_directors_table(directors):  # funkcija laukianti parametro
    query = """INSERT INTO directors (directorsId, Name) 
                      VALUES(?, ?)"""
    params = (directors.directorsId, directors.Name)  # paduodu funkcijos laukiamo parametro reiksmes
    query_database(query, params)


def insert_directors_movies(Name, movie_name):
    query = """INSERT INTO directors_movies (directorsId, moviesId)
                                        SELECT(SELECT directorsId FROM directors WHERE Name=?), 
                                        (SELECT moviesId FROM movies WHERE movie_name=?)"""
    params = (Name, movie_name)
    query_database(query, params)


def get_directors_table():
    query = "SELECT * FROM directors"
    query_database(query)


def get_directors_movies_table():
    query = "SELECT * FROM directors_movies"
    query_database(query)


def update_directors_table(director):
    query = "UPDATE director SET Name = ? WHERE directorsId = ?"
    params = (director.Name, director.directorsId)
    query_database(query, params)


def delete_directors_table(directorsId):
    query = "DELETE FROM directors WHERE directorsId = ?"
    params = (directorsId,)  # python tuple, jei be skliaustu ir kablelio, butu  variable
    query_database(query, params)

create_directors_table()
create_directors_movies_table()
# query_database("PRAGMA table_info(directors)")
# query_database("PRAGMA table_info(directors_movies)")
directors1 = Director(None, "Pirmas")
# insert_into_directors_table(directors1)
insert_directors_movies("Pirmas", "update Test")
get_directors_table()
get_directors_movies_table()