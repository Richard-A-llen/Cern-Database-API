import sqlite3

def get_database():
    connection = sqlite3.connect("cern.py")
    return connection

# The name of the table is 'userFiles'
def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS userFiles(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT NOT NULL,
              format TEXT NOT NULL,
              size INTEGER NOT NULL
        )        
        """
    ]  

    database = get_database()
    cursor = database.cursor()

    for table in tables:
        cursor.execute(table)
