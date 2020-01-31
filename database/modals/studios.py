from database.database import create_table_database, query_database
from entities.studio import Studio


def create_studios_table():
    query = """CREATE TABLE IF NOT EXISTS studios (
                        studioId INTEGER PRIMARY KEY AUTOINCREMENT,
                        studioName TEXT)"""
    create_table_database(query)


def insert_intoStudio_table(studio):  # funkcija laukianti parametro
    query = """INSERT INTO studios (studioId, studioName) 
                      VALUES(?, ?)"""
    params = (studio.studioId, studio.studioName)  # paduodu funkcijos laukiamo parametro reiksmes
    query_database(query, params)


def get_studio_table():
    query = "SELECT * FROM studios"
    query_database(query)

def update_studio_table(studio):
    query = "UPDATE studios SET studioName = ? WHERE studioId = ?"
    params = (studio.studioName, studio.studioId)
    query_database(query, params)

def delete_studio_table(studioId):
    query = "DELETE FROM studios WHERE studioId = ?"
    params = (studioId, ) #python tuple, jei be skliaustu ir kablelio, butu  variable
    query_database(query, params)


# query_database("PRAGMA table_info(studios)")
create_studios_table()
studio1 = Studio(None, "Warner Bros")
# insert_intoStudio_table(studio1)
studio2 = Studio(None, "Bross")
# insert_intoStudio_table(studio2)
studio3 = Studio(1, "UpdateTest")
# update_studio_table(studio3)
# delete_studio_table(3)

get_studio_table()
