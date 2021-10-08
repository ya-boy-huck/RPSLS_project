from human import Human
from ai import AI

class Player:

    def __init__(self):
        self.gesture = ["Rock", "Scissors", "Paper" , "Lizard", "Spock"]
        self.winner_of_round = ()
        self.rules = ()
        
    
    def gesture(self):
        self.gesture = input("Enter 0 for Rock, 1 for Scissors, 2 for Paper, 3 for Lizard, 4 for Spock")
        if self.gesture == "0":
            print(f"You have chosen {self.gesture[0]}")
        if self.gesture == "1":
            print(f"You have chosen {self.gesture[1]}")
        if self.gesture == "2": 
            print(f"You have chosen {self.gesture[2]}")
        if self.gesture == "3":        
            print(f"You have chosen {self.gesture[3]}")

    def winner_of_round(self):
        if self.human_player_point == +1:
            self.human_player_point.name = winner_of_round
        elif self.ai_player_point == +1:
            self.ai_player_point.name = winner_of_round    

        
    
    def rules(self):
        player_point = 0
        for player_point in self.player_point:
            while player_point <=1:
                print("Try again")
            else: 
                player_point == 2
                print[f"Congradulations Player {self.winner_of_game}, you have won the game"]
  
        for gesture in self.gesture:
           if [0] < [1]:
               player_point += 1
               print[f"Player {self.winner_of_round} has won the round"]
               return player_point
           elif [1] < [2]:
               player_point += 1
               print[f"Player {self.winner_of_round} has won the round"]
               return player_point
           elif [2] < [0]: 
               player_point += 1
               print[f"Player {self.winner_of_round} has won the round"]
               return player_point
           elif [0] < [3]: 
               player_point += 1
               print[f"Player {self.winner_of_round} has won the round"]
               return player_point
           elif [3] < [4]: 
               player_point += 1
               print[f"Player {self.winner_of_round} has won the round"]
               return player_point
           elif [4] < [1]: 
               player_point += 1
               print[f"Player {self.winner_of_round} has won the round"]
               return player_point
           elif [1] < [3]:
               player_point += 1
               print[f"Player {self.winner_of_round} has won the round"]
               return player_point
           else:
               gesture == gesture
               print("There has been a tie, try again.")






