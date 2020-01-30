from database.database import create_table_database, query_database
from entities.actor import Actor


def create_actors_table():
    query = """CREATE TABLE IF NOT EXISTS actors (
                        actorsId INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT)"""
    create_table_database(query)



def create_actors_movies_table():
    query = """CREATE TABLE IF NOT EXISTS actors_movies (
                        actors_movies_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        actorsId INTEGER,
                        moviesId INTEGER,
                        FOREIGN KEY (actorsId) REFERENCES actors(actorsId),
                        FOREIGN KEY (moviesId) REFERENCES movies(moviesId))"""
    create_table_database(query)

def insert_into_actors_table(actor):  # funkcija laukianti parametro
    query = """INSERT INTO actors (actorsId, name) VALUES(?, ?)"""
    params = (actor.actorsId, actor.name)  # paduodu funkcijos laukiamo parametro reiksmes
    query_database(query, params)

def insert_actors_movies(name, movie_name):
    query = """INSERT INTO actors_movies (actorsId, moviesId)
                                        SELECT(SELECT actorsId FROM actors WHERE name=?), 
                                        (SELECT moviesId FROM movies WHERE movie_name=?)"""
    params = (name, movie_name)
    query_database(query, params)

def get_actors_movies_table():
    query = "SELECT * FROM actors_movies"
    query_database(query)


def update_actors_table(actor):
    query = "UPDATE actors SET name = ? WHERE actorsId = ?"
    params = (actor.name, actor.actorsId)
    query_database(query, params)


def delete_actors_table(actorsId):
    query = "DELETE FROM actors WHERE actorsId = ?"
    params = (actorsId,)  # python tuple, jei be skliaustu ir kablelio, butu  variable
    query_database(query, params)


# create_table_database("DROP TABLE actors")
# query_database("PRAGMA table_info(actors)")
# query_database("PRAGMA table_info(actors_movies)")
create_actors_table()
create_actors_movies_table()
actor1 = Actor(None, "Julija Roberts")
actor2 = Actor(None, "Aidas Puskunigis")
# insert_into_actors_table(actor1)
# insert_into_actors_table(actor2)
actor3 = Actor(3, "Irma Aite")
# update_actors_table(actor3)
# delete_actors_table(2)
insert_actors_movies("Aidas Puskunigis", "pirmas")
get_actors_table()
get_actors_movies_table()
