from db_and_table import get_database

def insert_file(name, format, size):
    "Receives the file data and inserts it in the database"
    database = get_database()
    cursor = database.cursor()
    statement = "INSERT INTO userFiles(name, format, size) VALUES(?, ?, ?)"
    cursor.execute(statement, [name, format, size])
    database.commit()
    return True

def update_file(id, name, format, size):
    "Updates a file"
    database = get_database()
    cursor = database.cursor()
    statement = "UPDATE userFiles SET name=?, format=?, size=? WHERE id=?"
    cursor.execute(statement, [name, format, size, id])
    database.commit()
    return True

def delete_file(id):
    "Deletes a file by id"
    database = get_database()
    cursor = database.cursor()
    statement = "DELETE FROM userFiles WHERE id=?"
    cursor.execute(statement, [id])
    database.commit()
    return True    

def get_file_by_id(id): # Select operation
    "Returns a file by id"
    database = get_database()
    cursor = database.cursor()
    statement = "SELECT id, name, format, size FROM userFiles WHERE id=?"
    cursor.execute(statement, [id])
    return cursor.fetchone()

def get_files(): 
    "Returns all existing files"
    database = get_database()
    cursor = database.cursor()
    statement = "SELECT id, name, format, size FROM userFiles" 
    cursor.execute(statement)
    return cursor.fetchall()  























# creating REST API 
# using Flask and SQLite3 (for data)
# using JSON for data communication
# HTTP verbs(GET, POST, PUT and DELETE)which will be related to the CRUD of the database.
# 

