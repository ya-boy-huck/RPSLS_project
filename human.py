from player import Player

class Human(Player):
    
    def __init__(self):
        self.choose_gesture()
        super().__init__()

    # def human_player(self):
    #     self.human_player__name__ = input("Please type your name.")
    #     print(f"{self.human_player.__name__} has entered the game.")

    # def human_player_point(self):
    #     self.human_player_point() == Player.rules.player_point()
    #     print({[]}) 
        
    # def winner_of_round(self, rules):
    #     if self.human_player_point == +1:
    #         self.human_player_point = self.human_player.__name__
    #         print(f"{self.human_player.__name__} has won this round")
            