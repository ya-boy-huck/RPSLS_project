<<<<<<< HEAD
from player import player
class AI:
=======
from player import Player
import random

class AI (Player):
    def __init__(self):
        super().__init__()    
>>>>>>> 7288f550435c4f0a98bc2cf54087c3b86f8decde
    
    def human_turn(self):
        #human_gesture = Player.gesture()
        pass

    def ai_turn(self):
        #ai_gesture = random.randint(0,1,2,3,4)
        pass

    def winner_of_round(self):
        self.ai_player_point == +1
        self.ai_player_point.name = ai_player_winner