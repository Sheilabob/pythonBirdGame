player_list = []


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
    player_list.append(user)
    return user


def login():
    print("login")


def score_sort_key(e):
    return e["score"]


def show_scores():
    player_dict_list = []
    for player in range(len(player_list)):
        player_dict = {}
        player_dict["name"] = list(player_list)[player].name
        player_dict["score"] = list(
            player_list)[player].score
        player_dict_list.append(player_dict)
    player_dict_list.sort(reverse=True, key=score_sort_key)

    print("\n\t\t\tScoreBoard\n")
    print("\t\tNAME\t\t\tSCORE")
    print("\t______________________________________________\n")
    for player in range(len(player_dict_list)):
        print(
            f"\t\t{player_dict_list[player]['name']}\t\t\t{player_dict_list[player]['score']}\n")
    print("\t______________________________________________\n")
    input("Press any key to continue.\t")


def exit_game():
    print("exit game")
