from bird_pkg import birddetails
from playsound import playsound

import random


class Question:
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

            print(f"\n\n\tWhich bird do you hear?")
            print(f"\t\t1. {current_choices[0]}")
            print(f"\t\t2. {current_choices[1]}")
            print(f"\t\t3. {current_choices[2]}\n\n")

            playsound(current_bird['sound_location'])

            user_answer = input("\tYour answer:\t")
            if user_answer == str(current_choices.index(current_bird['name']) + 1):
                print("yay")
                player.score += 10
                print(player.name, player.score)
            else:
                print("sorry")

        print(f"Great Job, {player.name}!  Your score is: {player.score}")
        play_again = input("Would you like to play again (y/n)?\t")
        if play_again == "y":
            return True
        if play_again == "n":
            return False
