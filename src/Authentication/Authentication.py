import csv
import Classes as Cls
import Database.database_managment as DB
import sqlite3


def add_user(details: list):
    """Function creates a new account and adds in to the database."""

    # with open('users.csv', 'a', newline='') as file:
    #     csv_writer = csv.writer(file, delimiter=',')
    #     csv_writer.writerow(details)
    # file.close()

    DB.sql_add_user(details)


def create_user_object(user_name):
    """If user logs in successfully, this function creates a user object.
    If an admin attribute is 1 (int), the function creates Administrator object.
    If it is 0 (int), the function creates User object."""

    conn = sqlite3.connect('C:/Users/grzeg/PycharmProjects/Authentication/'
                           'database_file.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM users;""")
    rows = c.fetchall()
    for row in rows:
        if row[2] == user_name:
            # The user has an administrator status.
            if row[4] == 1:
                user_object = Cls.Administrator(row[2], row[3], row[0],
                                                row[1], row[4])
                return user_object
            # The user does not have an administrator status.
            else:
                user_object = Cls.User(row[2], row[3], row[0],
                                                row[1], row[4])
                return user_object

    # with open('users.csv') as file:
    #     csv_reader = csv.reader(file, delimiter=',')
    #     for line in csv_reader:
    #         if line[0] == user_name:
    #             # The user has an administrator status.
    #             if line[4] == 1:
    #                 user_object = Cls.Administrator(line[2], line[3], line[0],
    #                                                 line[1], line[4])
    #                 return user_object
    #             # The user does not have an administrator status.
    #             else:
    #                 user_object = Cls.User(line[2], line[3], line[0], line[1],
    #                                        line[4])
    #                 return user_object




