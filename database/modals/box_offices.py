from database.database import create_table_database
from entities.box_office import BoxOffice


def create_box_offices_table():
    query = """CREATE TABLE IF NOT EXISTS box_offices (
                        boxOfficeId INTEGER PRIMARY KEY AUTOINCREMENT,
                        gross REAL"""

    create_table_database(query)

def insert_into_box_offices_table(boxoffices):  # funkcija laukianti parametro
    query = """INSERT INTO box_offices (boxofficeId, gross) 
                      VALUES(?, ?)"""
    params = (boxoffices.boxofficeId, boxoffices.gross)  # paduodu funkcijos laukiamo parametro reiksmes
    query_database(query, params)


def get_box_offices_table():
    query = "SELECT * FROM box_offices"
    query_database(query)

def update_box_offices_table(boxoffices):
    query = "UPDATE box_offices SET gross = ? WHERE boxofficeId = ?"
    params = (boxoffices.gross, boxoffices.boxofficeId)
    query_database(query, params)

def delete_box_offices_table(boxofficeId):
    query = "DELETE FROM box_offices WHERE boxofficeId = ?"
    params = (boxofficeId, ) #python tuple, jei be skliaustu ir kablelio, butu  variable
    query_database(query, params)


# create_table_database("DROP TABLE box_offices")
# query_database("PRAGMA table_info(box_offices)")
create_box_offices_table()
boxoffices1 = BoxOffice(None, 35000)
# insert_into_box_offices_table(boxoffices1)
boxoffices2 = BoxOffice(None, 19000)
# insert_into_box_offices_table(boxoffices2)
boxoffices3 = BoxOffice(2, 999999)
update_box_offices_table(boxoffices3)
boxoffices4 = BoxOffice(None, 555555)
# insert_into_box_offices_table(boxoffices4)
delete_box_offices_table(4)
get_box_offices_table()
