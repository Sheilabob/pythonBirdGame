from bird_pkg import birddetails, questions
from playsound import playsound
import random


new_question = questions.Question()
new_question.generate_question()


class Player():
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.score = 0
