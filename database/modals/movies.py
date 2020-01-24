from database.database import create_table_database


def create_movies_table():
    query = """CREATE TABLE IF NOT EXISTS movies (
                        moviesId INTEGER PRIMARY KEY AUTOINCREMENT,
                        movie_name TEXT,
                        release_date DATE,
                        rating REAL,
                        genre TEXT,
                        box_office_name TEXT,
                        studioName TEXT)"""
    create_table_database(query)


create_movies_table()
