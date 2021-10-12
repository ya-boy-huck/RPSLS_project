from player import Player
import random

class AI (Player):
    def __init__(self):
        super().__init__()
        
    def choose_gesture(self):
        self.ai_turn = random.choice(["Rock", "Scissors", "Paper" , "Lizard", "Spock"])
        print(f"The Computer chose {self.ai_turn%[0]}")