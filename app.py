from bird_pkg import questions, players, modes

game_time = True
still_playing = True


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
            continue
        elif user_sel == 4:
            exit_game()
            break
        else:
            print("Invalid Selection.  Please try again")
    if game_time == False:
        break

    while True:
        modes.show_mode_menu()
        user_sel = int(input("\tPlease make a selection:\t"))
        if user_sel == 1:
            new_question = questions.Question()
            still_playing = new_question.generate_question(current_player)
            if still_playing == True:
                continue
            break
        elif user_sel == 2:
            new_fact = questions.Question()
            still_playing = new_fact.teach_me_something()
            if still_playing == True:
                continue
            break
        elif user_sel == 3:
            players.show_scores()
            continue
        elif user_sel == 4:
            current_player = None
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
        print("Logging out.")
        continue
