# from human import Human
# from ai import AI

class Player:

    def __init__(self):
         self.rules = ()
         self.gesture = ["Rock", "Scissors", "Paper" , "Lizard", "Spock"]
       
        
<<<<<<< HEAD
        
=======
    
    def gesture(self):
     while True:
        self.gesture = input("Enter 0 for Rock, 1 for Scissors, 2 for Paper, 3 for Lizard, 4 for Spock")
        if self.gesture == "0":
            print(f"You have chosen {self.gesture[0]}")
        if self.gesture == "1":
            print(f"You have chosen {self.gesture[1]}")
        if self.gesture == "2": 
            print(f"You have chosen {self.gesture[2]}")
        if self.gesture == "3":        
            print(f"You have chosen {self.gesture[3]}")
        if self.gesture.lower() not in ('0','1', '2', '3', '4'):
                     print("Please try again and Enter 0 for Rock, 1 for Scissors, 2 for Paper, 3 for Lizard, 4 for Spock")
        else:
            break

    def winner_of_round(self):
        if self.human_player_point == +1:
            self.human_player_point.name = winner_of_round
        elif self.ai_player_point == +1:
            self.ai_player_point.name = winner_of_round          
>>>>>>> 7288f550435c4f0a98bc2cf54087c3b86f8decde
    def rules(self):
        player_point = 0
        for player_point in self.player_point:
            while player_point <= 1:
                print("Try again")
            else: 
                player_point == 2
                print[f"Congratulations Player {self.winner_of_game}, you have won the game"]
  
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
           elif [3] < [2]: 
               player_point += 1
               print[f"Player {self.winner_of_round} has won the round"]
               return player_point
           elif [2] < [4]: 
               player_point += 1
               print[f"Player {self.winner_of_round} has won the round"]
               return player_point
           elif [4] < [0]:
               player_point += 1
               print[f"Player {self.winner_of_round} has won the round"]
               return player_point  
           else:
               gesture == gesture
               print("There has been a tie, try again.")


    def gesture(self):
        while True:
            self.gesture = input("Enter 0 for Rock, 1 for Scissors, 2 for Paper, 3 for Lizard, 4 for Spock")
           
            if self.gesture.lower() not in ('0','1', '2', '3', '4'):
                     print("Please try again and Enter 0 for Rock, 1 for Scissors, 2 for Paper, 3 for Lizard, 4 for Spock")
            else:
                break 



<<<<<<< HEAD
=======

>>>>>>> 7288f550435c4f0a98bc2cf54087c3b86f8decde
