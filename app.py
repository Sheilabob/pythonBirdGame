from bird_pkg import birddetails, questions, players, modes
from playsound import playsound
import random

game_time = True


def exit_game():
    print("\nExiting Game.\nThank you for playing!")
    global game_time
    game_time = False


while True:
    restart = False
    current_player = None
    print("\n\n\t      Hello!  Welcome to the Bird Sounds Game!")
    players.show_user_menu()

    while True:
        user_sel = int(input("\tPlease make a selection:\t"))
        if user_sel == 1:
            current_player = players.create_user()
            break
        elif user_sel == 2:
            current_player = players.login()
            break
        elif user_sel == 3:
            players.show_scores()
            break
        elif user_sel == 4:
            exit_game()
            break
        else:
            print("Invalid Selection.  Please try again")
    if game_time == False:
        break
    modes.show_mode_menu()

    while True:
        user_sel = int(input("\tPlease make a selection:\t"))
        if user_sel == 1:
            new_question = questions.Question()
            game_time = new_question.generate_question(current_player)
            break
        elif user_sel == 2:
            modes.learn_mode()
            break
        elif user_sel == 3:
            players.show_scores()
            break
        elif user_sel == 4:
            restart = True
            break
        elif user_sel == 5:
            exit_game()
            break
        else:
            print("Invalid Selection.  Please try again")
    if game_time == False:
        break
    if restart == True:
        print("restart is true")
        continue
