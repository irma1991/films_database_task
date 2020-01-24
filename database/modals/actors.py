from database.database import create_table_database


def create_actors_table():
    query = """CREATE TABLE IF NOT EXISTS actors (
                        actorsId INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT)"""
    create_table_database(query)


create_actors_table()

def create_actors_movies_table():
    query = """CREATE TABLE IF NOT EXISTS actors_movies (
                        actors_movies_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        actorsId FOREIGN KEY (actorsId) REFERENCES actors(actorsId),
                        moviesId FOREIGN KEY (moviesId) REFERENCES movies(moviesId))"""
    create_table_database(query)


create_actors_movies_table()
