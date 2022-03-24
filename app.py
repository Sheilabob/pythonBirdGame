from bird_pkg import birddetails
from playsound import playsound
import random


# bird_list = ['./sounds/chickadee.mp3',
#              './sounds/downyWoodpecker.mp3', './sounds/finch.mp3']

# bird_options = {
#     "chickadee": {
#         "name": "chickadee",
#         "sound_location": "./sounds/chickadee.mp3",
#         "hints": ["This is a medium-sized bird.", "It has a black cap on its head.", "It is in a bush in an open forest area."],
#         "index": 1,
#         "not_played_yet": True,
#     },
#     "downy_woodpecker": {
#         "name": "downy woodpecker",
#         "sound_location": "./sounds/downyWoodpecker.mp3",
#         "hints": ["This is a medium-sized bird.", "It has a dagger-shaped beak.", "It is on the trunk of a tree in a forest."],
#         "index": 2,
#         "not_played_yet": True,
#     },
#     "finch": {
#         "name": "finch",
#         "sound_location": "./sounds/finch.mp3",
#         "hints": ["This is a medium-sized bird.", "It is red and brown in color.", "It is sitting on a feeder in someone's backyard."],
#         "index": 3,
#         "not_played_yet": True,
#     }
# }

print(f"{birddetails.bird_options.get('finch')['sound_location']}")

playsound(birddetails.bird_options.get('finch')['sound_location'])
# def play_bird():
#     this_time = random.choice(bird_list)
#     playsound(this_time)


# play_bird()


# playsound('./sounds/chickadee.mp3')
# playsound('./sounds/downyWoodpecker.mp3')
# playsound('./sounds/finch.mp3')
