from colorama import init, Fore, Style
init(autoreset=True)


player_list = []
index_of_user = 0


def search_playerlist(user):
    for player in range(len(player_list)):
        if user == list(player_list)[player].name:
            return list(player_list)[player]
    return None

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


def sort_part(the_list, low_idx, pivot_idx):
    pivot_val = the_list[pivot_idx].score
    store_pivot_idx = the_list[pivot_idx]

    while pivot_idx != low_idx:
        low_val = the_list[low_idx].score
        store_low_idx = the_list[low_idx]

        if low_val >= pivot_val:
            low_idx += 1
        else:
            the_list[low_idx] = the_list[pivot_idx-1]
            the_list[pivot_idx] = store_low_idx
            the_list[pivot_idx-1] = store_pivot_idx
            pivot_idx -= 1

    return pivot_idx


def quicksort(the_list, low_idx, high_idx):
    if low_idx > high_idx:
        return

    pivot_idx = sort_part(the_list, low_idx, high_idx)
    quicksort(the_list, low_idx, pivot_idx-1)
    quicksort(the_list, pivot_idx+1, high_idx)


def show_user_menu():
    print(Fore.CYAN + Style.BRIGHT + "\n\t\t           User Menu")
    print(Fore.CYAN + Style.BRIGHT + "\t\t ---------------------------------")
    print(Fore.CYAN + Style.BRIGHT + "\t\t|  1. Register   |  2. Login      |")
    print(Fore.CYAN + Style.BRIGHT + "\t\t ---------------------------------")
    print(Fore.CYAN + Style.BRIGHT + "\t\t|  3. Scoreboard |  4. Exit       |")
    print(Fore.CYAN + Style.BRIGHT + "\t\t ---------------------------------\n")


class Player():
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.score = 0


def create_user():
    while True:
        print(Fore.CYAN + Style.BRIGHT + "\nRegistration")
        user_name = input(Fore.CYAN + Style.BRIGHT +
                          "Please enter your name:\t")
        if len(user_name) > 12 or user_name[0].isalpha() == False:
            print(Fore.RED + Style.BRIGHT +
                  "\nPlease choose a username that begins with a letter and is 12 characters or less in length.")
            continue
        user = search_playerlist(user_name)
        if user != None:
            print(Fore.RED + Style.BRIGHT + "\nSorry, this username is already in use. If you are already registered, please login.  Otherwise, please select a different user name.")
            return None
        while True:
            user_password = input(
                Fore.CYAN + Style.BRIGHT + "Please choose a password:\t")
            if len(user_password) < 6:
                print(
                    Fore.RED + Style.BRIGHT + "\nPlease choose a password that is at least 6 characters in length.")
                continue
            break
        user = Player(user_name, user_password)
        print(Fore.GREEN + Style.BRIGHT + f"\nWelcome, {user.name}!")
        print(Fore.GREEN + Style.BRIGHT + "You are logged in.")
        player_list.append(user)
        return user


def login():
    print("\nLogin")
    user_name = input(Fore.CYAN + Style.BRIGHT + "Username:\t")
    user = search_playerlist(user_name)
    if user == None:
        print(Fore.RED + Style.BRIGHT + "\nSorry: username not found.")
        return None
    user_password = input(Fore.CYAN + Style.BRIGHT + "Password:\t")
    if user_password == user.password:
        print(Fore.GREEN + Style.BRIGHT + f"\nWelcome back, {user.name}!")
        print(Fore.GREEN + Style.BRIGHT + "You are logged in.")
        return user
    else:
        print(Fore.RED + Style.BRIGHT +
              "\nYou have entered an incorrect password.")


def score_sort_key(e):
    return e["score"]


def show_scores():

    quicksort(player_list, 0, len(player_list)-1)
    score_list = list(player_list)

    print(Fore.YELLOW + Style.BRIGHT + "\n\t\t\tScoreBoard\n")
    print(Fore.YELLOW + Style.BRIGHT + "\t\tNAME\t\t\tSCORE")
    print(Fore.YELLOW + Style.BRIGHT +
          "\t______________________________________________\n")
    for player in range(0, len(score_list)):
        print(Fore.YELLOW + Style.BRIGHT +
              f"\t\t{score_list[player].name}\t\t\t{score_list[player].score}\n")
    print(Fore.YELLOW + Style.BRIGHT +
          "\t______________________________________________\n")
    input(Fore.CYAN + Style.BRIGHT + "Press enter to continue.\t")

    # Below is a working sort using the built-in python sort method.  As an exercise, I replaced it with a quicksort, but left the code here to show another approach

    # player_dict_list = []
    # for player in range(len(player_list)):
    #     player_dict = {}
    #     player_dict["name"] = list(player_list)[player].name
    #     player_dict["score"] = list(
    #         player_list)[player].score
    #     player_dict_list.append(player_dict)
    # player_dict_list.sort(reverse=True, key=score_sort_key)

    # print("\n\t\t\tScoreBoard\n")
    # print("\t\tNAME\t\t\tSCORE")
    # print("\t______________________________________________\n")
    # for player in range(len(player_dict_list)):
    #     print(
    #         f"\t\t{player_dict_list[player]['name']}\t\t\t{player_dict_list[player]['score']}\n")
    # print("\t______________________________________________\n")
    # input("Press any key to continue.\t")


def exit_game():
    print("exit game")
