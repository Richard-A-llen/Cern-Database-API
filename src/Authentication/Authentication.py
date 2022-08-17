import csv
import Classes as Cls
import sqlite3


def add_user(details: list):
    """Function creates a new account and adds in to the database."""
    # it adds it to the file for now!

    with open('users.csv', 'a', newline='') as file:
        csv_writer = csv.writer(file, delimiter=',')
        csv_writer.writerow(details)
    file.close()


def create_user_object(user_name):
    """If user logs in successfully, this function creates a user object.
    If an admin attribute is True, the function creates Administrator object.
    Otherwise, the function creates User object."""

    with open('users.csv') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for line in csv_reader:
            if line[0] == user_name:
                # The user has an administrator status.
                if line[4] == 1:
                    user_object = Cls.Administrator(line[2], line[3], line[0],
                                                    line[1], line[4])
                    return user_object
                # The user does not have an administrator status.
                else:
                    user_object = Cls.User(line[2], line[3], line[0], line[1],
                                           line[4])
                    return user_object


