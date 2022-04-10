def show_user_menu():
    print("\n\t\t           User Menu")
    print("\t\t ---------------------------------")
    print("\t\t|  1. Register   |  2. Login      |")
    print("\t\t ---------------------------------")
    print("\t\t|  3. Scoreboard |  4. Exit       |")
    print("\t\t ---------------------------------\n")


class Player():
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.score = 0


def create_user():
    print("\nRegistration")
    user_name = input("Please enter your name:\t")
    user_password = input("Please choose a password:\t")
    user = Player(user_name, user_password)
    print(f"\nWelcome, {user.name}!")
    print("You are logged in.")
    return user


def login():
    print("login")


def show_scores():
    print("show scores")


def exit_game():
    print("exit game")
