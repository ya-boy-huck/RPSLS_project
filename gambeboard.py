
from player import Player
from human import Human
from AI import AI

class Gameboard:        

    def __init__(self):
        self.winner_of_game = ()

  
    
    
        def winner_of_game(self):
            if self.human_player_point >= 2:
                self.human_player_point.name = winner_of_round
            elif self.ai_player_point >= 2:
                self.ai_player_point.name = winner_of_round
            else:
                print("The game continues!") 
    