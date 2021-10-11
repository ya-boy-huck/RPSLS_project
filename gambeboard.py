
from player import Player
from human import Human
from AI import AI

class Gameboard:        

    def __init__(self):
        self.winner_of_game = ()

    #def game_sequence(self):
        #human_gesture = Player.gesture()
        #ai_gesture = random.randint(0,1,2,3,4)
        #pass
  
    
    
    def winner_of_game(self):
        if self.human_player_point >= 2:
            self.human_player_point.name = winner_of_round
        elif self.ai_player_point >= 2:
            self.ai_player_point.name = winner_of_round
        else:
            print("The game continues!") 
    