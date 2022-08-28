from db_and_table import get_database
# using 'db_and_table.py' to access 'get_database' function

def insert_file(name, format, subject):
    # calling get_database() method from 'db_and_table.py'
    database = get_database()  
    cursor = database.cursor()
    statement = "INSERT INTO userfiles(name, format, subject) VALUES(?, ?, ?)"    
    cursor.execute(statement, [name, format, subject])
    # makes permanent the changes
    database.commit()  
    return True

def update_file(id, name, format, subject):    
    database = get_database()    
    cursor = database.cursor()
    statement = "UPDATE userfiles SET name=?, format=?, subject=? WHERE id=?"
    cursor.execute(statement, [name, format, subject, id])
    database.commit()
    return True

def delete_file(id):
    "Deletes a file by id"
    database = get_database() 
    cursor = database.cursor()
    statement = "DELETE FROM userfiles WHERE id=?"
    # executes the statement and fetch the records from the database. 
    cursor.execute(statement, [id]) 
    database.commit() 
    return True    

def get_file_by_id(id):     
    database = get_database()
    cursor = database.cursor()
    statement = "SELECT id, name, format, subject FROM userfiles WHERE id=?"
    # executes the query based on id and fetch the records from the database.
    cursor.execute(statement, [id]) 
    # returns one row of the query (statement)
    return cursor.fetchone() 

def get_files(): 
    "Returns all existing files"
    database = get_database()
    cursor = database.cursor()
    statement = "SELECT id, name, format, subject FROM userfiles" 
    cursor.execute(statement)
    # returns all the rows of the query (statement)
    return cursor.fetchall()  


# Calling some functions
insert_file("DarkMatter", ".pdf", "Physics")
insert_file("Magnets", ".jpg", "Engineering")
insert_file("Web", ".docx", "Computing")
get_files()
get_file_by_id(2)

