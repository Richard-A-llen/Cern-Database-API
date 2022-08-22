import Authentication_checker as Ac
from Authentication_checker import hashing


def log_in():
    """This is a log-in checker function that examines inputs provided by the
    user before the user object is created."""

    def username_fn():
        """The function checks if username is provided correctly and if it
        exists in the database."""

        inp = input(' Provide your username: ')
        # correct format of username?
        if len(inp.split()) != 1:
            print("No space are allowed, try again")
            inp = username_fn()
        # does username exist in the database?
        user_name_verification = Ac.user_exists(inp)
        # if user_name_verification is not 1:
        if user_name_verification != 1:
            print('the user name does not exist. Try again.')
            inp = username_fn()

        return inp

    def password_fn(username):
        """The function checks if password of a user is provided correctly."""

        inp = input(' Provide your password: ')
        password_verification = Ac.password_correct(username, inp)
        if password_verification is not True:
            print(' Wrong password, please try again.')
            password_fn(username)
        return hashing(inp)

    username = username_fn()
    password = password_fn(username)
    return [username, password]


def sing_up():
    """This is a sign-up checker function that examines inputs provided by the
        user before the sign-up details are passed through."""

    def name_fn():
        """The function checks if name of the user is provided correctly."""

        inp = input(" Provide your name: ")
        if len(inp.split()) != 2:
            print(" Provide your first name and surname separated by space! "
                  "Try again.")
            inp = name_fn()
        return inp

    def email_fn():
        """The function checks if e-mail of the user is provided correctly."""

        inp = input(' Provide your e-mail address: ')
        # if "@cern.ch" not in inp:
        if not inp.endswith("@cern.ch"):
            print(" Wrong e-mail! Try again.")
            inp = email_fn()
        return inp

    def username_fn():
        """The function checks if username is provided correctly."""

        inp = input(' Provide your username: ')
        # is the username a singe word (no spaces)?
        if len(inp.split()) != 1:
            print(" No space is allowed, try again")
            inp = username_fn()
        # does the username name exist in the database?
        if Ac.user_exists(inp) == 1:
            print('User name already exists. Provide a different one: ')
            inp = username_fn()
        return inp

    def password_fn():
        """The function checks if password of a user is provided correctly."""
        inp = input(' Provide your password: ')
        # checks if the password is strong enough
        check_list = Ac.password_strength(inp)
        if check_list[0] is False:
            print("Password is too short.")
            inp = password_fn()
        if check_list[1] is False:
            print("Password needs to have at least one lowercase character.")
            inp = password_fn()
        if check_list[2] is False:
            print("Password needs to have at least one uppercase character.")
            inp = password_fn()
        if check_list[3] is False:
            print("Password needs to have at least one number.")
            inp = password_fn()
        if check_list[4] is False:
            print("Password needs to have at least one special character.")
            inp = password_fn()
        return hashing(inp)

    name = name_fn()
    email = email_fn()
    username = username_fn()
    password = password_fn()
    return [username, password, name, email, 0]






