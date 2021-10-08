    def winner_of_round(self):
        if self.human_player_point == +1:
            self.human_player_point.name = winner_of_round
        elif self.ai_player_point == +1:
            self.ai_player_point.name = winner_of_round    
    
    
    def winner_of_game(self):
        if self.human_player_point >= 2:
            self.human_player_point.name = winner_of_round
        elif self.ai_player_point >= 2:
            self.ai_player_point.name = winner_of_round
        else:
            print("The game continues!") 
    