from bird_pkg import questions, players, modes
from colorama import init, Fore, Style
init(autoreset=True)

game_time = True
still_playing = True


def exit_game():
    print(Fore.RED + Style.BRIGHT + "\nExiting Game.\nThank you for playing!")
    global game_time
    game_time = False


while True:
    restart = False
    current_player = None
    print(Fore.CYAN + Style.BRIGHT +
          "\n\n      \U0001F986 \U0001F99C \U0001F985 Hello!  Welcome to the Bird Sounds Game! \U0001F9A2 \U0001F989 \U0001F99A")

    while True:
        players.show_user_menu()
        user_sel = input(Fore.CYAN + Style.BRIGHT +
                         "\tPlease make a selection:\t")
        if user_sel == '1':
            current_player = players.create_user()
            if current_player == None:
                continue
            break
        elif user_sel == '2':
            current_player = players.login()
            if current_player == None:
                continue
            break
        elif user_sel == '3':
            players.show_scores()
            continue
        elif user_sel == '4':
            exit_game()
            break
        else:
            print(Fore.RED + Style.BRIGHT +
                  "Invalid Selection.  Please try again")
    if game_time == False:
        break

    while True:
        modes.show_mode_menu()
        user_sel = input(Fore.CYAN + Style.BRIGHT +
                         "\tPlease make a selection:\t")
        if user_sel == '1':
            new_question = questions.Question()
            still_playing = new_question.generate_question(current_player)
            if still_playing == True:
                continue
            break
            # Code here is for testing purposes only(to prevent tester from having to play game to get score):
            # current_player.score += 10
            # print(current_player.name, current_player.score)
            # continue
        elif user_sel == '2':
            new_fact = questions.Question()
            still_playing = new_fact.teach_me_something()
            if still_playing == True:
                continue
            break
        elif user_sel == '3':
            players.show_scores()
            continue
        elif user_sel == '4':
            current_player = None
            restart = True
            break
        elif user_sel == '5':
            exit_game()
            break
        else:
            print(Fore.RED + Style.BRIGHT +
                  "Invalid Selection.  Please try again")
    if game_time == False:
        break
    if restart == True:
        print(Fore.RED + Style.BRIGHT + "Logging out.")
        continue
