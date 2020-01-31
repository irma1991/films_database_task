from datetime import date

from database.database import create_table_database, query_database
from entities.movie import Movie
from entities.studio import Studio
from entities.box_office import BoxOffice
from entities.director import Director
from entities.actor import Actor
from entities.genre import Genre

def create_movies_table():
    query = """CREATE TABLE IF NOT EXISTS movies (
                        moviesId INTEGER PRIMARY KEY AUTOINCREMENT,
                        movie_name TEXT,
                        release_date DATE,                        
                        rating REAL,
                        genre TEXT,
                        studioId INTEGER,
                        boxofficeId INTEGER,
                        directorsId INTEGER,
                        actorsId INTEGER,
                        genresId INTEGER,
                        FOREIGN KEY (studioId) REFERENCES studios(studioId),
                        FOREIGN KEY (boxofficeId) REFERENCES box_offices(boxofficeId),
                        FOREIGN KEY (directorsId) REFERENCES directors(directorsId),
                        FOREIGN KEY (actorsId) REFERENCES actors(actorsId),
                        FOREIGN KEY (genresId) REFERENCES genres(genresId)               
                       )"""
    create_table_database(query)


# create_movies_table)
# query_database("PRAGMA table_info(movies)")

def create_movie(movie, studio, boxOffice, director, actor, genre):
    query = """INSERT INTO movies VALUES (?, ?, ?, ?, ?),
            SELECT (SELECT studioId FROM studios WHERE studioName=(?)),
            SELECT (SELECT boxofficeId FROM box_offices WHERE gross=(?)),
            SELECT (SELECT directorsId FROM directors WHERE Name=(?)),
            SELECT (SELECT actorsId FROM actors WHERE name=(?)),
            SELECT (SELECT genresId FROM genres WHERE name=(?))
            """
    params = (movie.moviesId, movie.movie_name, movie.release_date, movie.rating, movie.genre,
              studio.studioId, studio.studioName,
              boxOffice.boxofficeId, boxOffice.gross,
              director.directorsId, director.Name,
              actor.actorsId, actor.name,
              genre.genresId, genre.name)

    query_database(query, params)

movie = Movie(None, "Pavadinimas", "Data", "Ivertinimas", "Zanras", None, None, None, None, None)
studio = Studio(None, "Studios pavadinimas")
boxOffice = BoxOffice(None, "1000")
director = Director(None, "Director pavadinimas")
actor = Actor(None, "Actor pavadinimas")
genre = Genre(None, "Genre pavadinimas")

create_movie(movie, studio, boxOffice, director, actor, genre)