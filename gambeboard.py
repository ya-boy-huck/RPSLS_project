
from player import Player
from human import Human
from AI import AI

class Gameboard:        

    def __init__(self):
        self.winner_of_game = ()
        self.player_one = Human()
        self.player_two = None

    def run_game(self):
        self.welcome_message()
        self.rules_explained()
        self.game_mode()

        # Intro phase
    def welcome_message(self): 
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
        # welcome message
    def rules_explained(self):
            print("Rock, Paper, Scissors, Lizard, Spock is the game of rock, paper, scissors woth a twist! Choose wether you would like to play with another person or against the computer. The first player to win 2 out of the 3 rounds will be crowned the winner! Here is some instructions for you to follow. Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard, Lizard poisons Spock, Spock smashes Scissors, Scissors decapitates Lizard, Lizard eats Paper, Paper disproves Spock, Spock vaporizes Rock. Now that has been explained, Enjoy the game!")
        # explain rules
    def game_mode(self):
        input("Enter 1 to play against another person, or enter 2 to challenge the computer!")
        if input == "1":
            self.player_two = Human()
        elif input == "2":
            self.player_two = AI()
        else:
            print("please enter the number 1 or 2 to continue")
        # choose game type - Assign a type to Player 2

        # Game round phase - Loop

        # P1 picks
        # P2 picks
        # Determine winner of round

        # Endgame
        # Display winner of game

        pass

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
    
    
    def winner_of_game(self):
        if self.human_player_point >= 2:
            self.human_player_point.name = winner_of_round
        elif self.ai_player_point >= 2:
            self.ai_player_point.name = winner_of_round
        else:
            print("The game continues!") 
    # def winner_of_game(self):
    #     if self.human_player_point >= 2:
    #         self.human_player_point.name = winner_of_round
    #     elif self.ai_player_point >= 2:
    #         self.ai_player_point.name = winner_of_round
    #     else:
    #         print("The game continues!") 
    