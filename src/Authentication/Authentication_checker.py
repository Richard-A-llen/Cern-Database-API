import csv
import hashlib as hl
import string as s
import Database.database_managment as DB


def hashing(password):
    password_hash = hl.sha256(str.encode(password)).hexdigest()
    return password_hash


def user_exists(user_name):
    """This function checks if user name exists. It returns true if it does,
    otherwise it return false."""

    # with open('users.csv') as file:
    #     csv_reader = csv.reader(file, delimiter=',')
    #     for line in csv_reader:
    #         if line[0] == user_name:
    #             return True
    #     return False

    result = DB.sql_user_exist(user_name)
    return result


def password_correct(user_name, password):
    """This function checks if user name exists. It returns true if it does,
    otherwise it return false."""

    result = DB.sql_password_correct(user_name)
    if result == hashing(password):
        return True
    else:
        return False

    # with open('users.csv') as file:
    #     csv_reader = csv.reader(file, delimiter=',')
    #     for line in csv_reader:
    #         if line[0] == user_name:
    #             if line[1] == hashing(password):
    #                 return True
    #             else:
    #                 return False


def password_strength(password):
    """This function checks if password is strong enough."""
    # write more!!!
    checking_list = [False] * 5
    number = 10
    # long enough check_list[0] is True
    if len(password) >= number:
        checking_list[0] = True
    # has at least one lowercase character
    for i in password:
        if i.islower():
            checking_list[1] = True
    # has at least one uppercase character
    for i in password:
        if i.isupper():
            checking_list[2] = True
    # has at least one number
    for i in password:
        if i.isnumeric():
            checking_list[3] = True
    # has at least one special character
    special_char = s.punctuation
    for i in password:
        if i in special_char:
            checking_list[4] = True

    return checking_list
