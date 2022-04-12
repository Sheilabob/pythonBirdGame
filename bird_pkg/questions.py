import random
from bird_pkg import birddetails
from playsound import playsound
from colorama import init, Fore, Style
init(autoreset=True)


class Question:
    # side note here: I now question the choice to treat a question as a class, but it may work if there are subclasses for learning, easy quiz questions and hard quiz questions
    def __init__(self):
        pass

    def generate_question(self, player):

        birdlist = birddetails.bird_options

        def populate_list(entry):
            return entry
        unplayed_birds = list(map(populate_list, birdlist))

        while len(unplayed_birds) > 0:

            current_choices = []

            def populate_names(entry):
                return entry['name']
            other_choices = list(map(populate_names, birdlist))
# side note here: after learning how to work with objects while setting up the player functions for this game: it might be easier to set up the birds as a list of objects and then just populate the current choices, other choices, and unplayed bird lists from that list of objects . . .
            current_bird = unplayed_birds[random.randint(
                0, len(unplayed_birds)-1)]
            current_choices.append(current_bird['name'])
            other_choices.pop(other_choices.index(current_bird['name']))
            unplayed_birds.remove(current_bird)

            choice2 = other_choices[random.randint(
                0, len(other_choices)-1)]

            other_choices.remove(choice2)
            current_choices.append(choice2)

            choice3 = other_choices[random.randint(
                0, len(other_choices)-1)]

            other_choices.remove(choice3)
            current_choices.append(choice3)

            random.shuffle(current_choices)

            print(Fore.MAGENTA + Style.BRIGHT +
                  f"\n\n\tWhich bird do you hear?")
            print(Fore.MAGENTA + Style.BRIGHT + f"\t\t1. {current_choices[0]}")
            print(Fore.MAGENTA + Style.BRIGHT + f"\t\t2. {current_choices[1]}")
            print(Fore.MAGENTA + Style.BRIGHT +
                  f"\t\t3. {current_choices[2]}\n\n")

            playsound(current_bird['sound_location'])

            user_answer = input(Fore.CYAN + Style.BRIGHT + "\tYour answer:\t")
            if user_answer == str(current_choices.index(current_bird['name']) + 1):
                print(Fore.GREEN + Style.BRIGHT +
                      "Great job!  You earned 10 points!")
                player.score += 10
                print(Fore.GREEN + Style.BRIGHT +
                      f"Your score is now: {player.score}")
            else:
                print(Fore.RED + Style.BRIGHT +
                      "Sorry, that was the wrong answer. \n\tThe correct answer was:", Fore.CYAN + Style.BRIGHT + current_bird['name'])

        print(Fore.GREEN + Style.BRIGHT +
              f"Great Job, {player.name}!  Your score is currently: {player.score}")
        play_again = input(Fore.CYAN + Style.BRIGHT +
                           "Would you like to play again (y/n)?\t")
        if play_again == "y":
            return True
        if play_again == "n":
            return False

    def teach_me_something(self):
        return_to_menu = False
        birdlist = birddetails.bird_options

        def populate_list(entry):
            return entry
        unplayed_birds = list(map(populate_list, birdlist))
        while len(unplayed_birds) > 0:
            learn = input(Fore.MAGENTA + Style.BRIGHT +
                          "\nWould you like to learn about a bird and its sound (y/n)?")
            if learn == 'y':
                current_bird = unplayed_birds[random.randint(
                    0, len(unplayed_birds)-1)]
                unplayed_birds.remove(current_bird)

                print(Fore.MAGENTA + Style.BRIGHT +
                      f"\n\tYou are hearing a {current_bird['name']}.")
                print(Fore.MAGENTA + Style.BRIGHT +
                      f"\n\t\tSome facts about the {current_bird['name']}:")
                label = 1
                for info in range(0, len(current_bird['hints'])):
                    print(Fore.MAGENTA + Style.BRIGHT +
                          f"\t\t\t{label}.\t{current_bird['hints'][info]}")
                    label += 1

                playsound(current_bird['sound_location'])
                input(Fore.CYAN + Style.BRIGHT + "Press enter to continue.")
            elif learn == 'n':
                return True
            else:
                print(Fore.RED + Style.BRIGHT +
                      "Sorry, that wasn't a valid entry.  Try again")
        if return_to_menu == True:
            return True
        input(Fore.CYAN + Style.BRIGHT +
              "\nThat's all the birds for now.  Press enter to return to the menu.\n")
        return True
