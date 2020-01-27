from database.database import create_table_database, query_database

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

    create_table_database(query)

# create_table_database("DROP TABLE movies")
query_database("PRAGMA table_info(movies)")
create_movies_table()
