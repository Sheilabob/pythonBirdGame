player_list = []
index_of_user = 0


def search_playerlist(user):
    for player in range(len(player_list)):
        if user == list(player_list)[player].name:
            return list(player_list)[player]
        else:
            print("Sorry: username not found.")
            return False

    # The following is NOT how to do this, but I left it in to show the twisted turns that I took trying to get to what was actually a very simple solution:
    # player_dict = {}
    # player_index_list = []
    # for player in range(len(player_list)):
    #     player_dict[list(player_list)[player].name] = list(
    #         player_list)[player].password
    #     player_index_list.append(list(player_list)[player].name)
    # if user in player_dict:
    #     index_of_user = player_index_list.index(user)
    #     return index_of_user
    # else:
    #     print("Sorry: username not found.")
    #     return False


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
    print("\nLogin")
    user_name = input("Username:\t")
    user = search_playerlist(user_name)
    user_password = input("Password:\t")
    if user_password == user.password:
        return user
    else:
        print("You have entered an incorrect password.")


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
