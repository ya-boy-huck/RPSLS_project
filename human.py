from player import Player
class Human:
    
    def __init__(self):
        self.human_player()
        self.human_player_point()
        self.winner_of_round(self)

    def human_player(self):
        self.human_player  == input("Please type your name.")
        self.human_player.input = self.human_player.__name__
        print(f"{self.human_player.__name__} has entered the game.")

    def human_player_point(rules):
        rules.human_player_point == Player.rules.player_point()
        return input 
        
    def winner_of_round(self, rules):
        self.human_player_point == +1
        self.human_player_point = self.human_player.__name__
        print(f"{self.human_player.__name__} has won this round")