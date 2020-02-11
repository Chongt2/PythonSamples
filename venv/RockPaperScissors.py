"""
Code by Tai-Yin Chong
Play Rock Paper Scissors
"""

import random

class Player:
    def __init__(self, name = "Your opponent"):
        self.name = name
    def roll(self):
        return random.randint(0,2)

class FirstPerson(Player):
    def roll(self, player_roll):
        if player_roll == "R":
            return 0
        elif player_roll == "P":
            return 1
        elif player_roll == "S":
            return 2

def determine_outcome(first_roll, second_roll):
    roll_matrix = [[0,-1,1],
               [1,0,-1],
               [-1,1,0]]
    result = roll_matrix[first_roll][second_roll]
    if result == -1:
        return "lost"
    elif result == 0:
        return "tied"
    elif result == 1:
        return "won"

roll_dictionary = {0:"Rock",1:"Paper",2:"Scissor"}
# What is your name?
your_name = input("What is your name?")
player_roll = input("What do you roll?\nRock: \"R\"\t Paper: \"P\"\t Scissor: \"S\"\n")
first_player = FirstPerson(your_name)
second_player = Player()
second_player_roll = second_player.roll()
outcome = determine_outcome(first_player.roll(player_roll),second_player_roll)
print("You played: " + roll_dictionary[first_player.roll(player_roll)])
print(second_player.name + " played: " +  roll_dictionary[second_player_roll])
print("You " + determine_outcome(first_player.roll(player_roll),second_player_roll))
if outcome == "won":
    print("Congratulations " + first_player.name + "!")