
from human import Human
from AI import AI
from player import Player


class Gameboard:        

    def __init__(self):
        self.player_one = Human()
        self.player_two = None
        self.player_point = 0
        self.gesture = None
        self.winner_of_round = None
        self.winner_of_game = None
        super().__init__()

    def run_game(self):
        self.welcome_message()
        self.rules_explained()
        self.game_mode()
        self.player_picks()
        self.rule_one()
        self.rule_two()
        
    # Intro phase
        # Intro phase
    def welcome_message(self): 
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
        # welcome message
    def rules_explained(self):
            print("Rock, Paper, Scissors, Lizard, Spock is the game of rock, paper, scissors woth a twist! Choose wether you would like to play with another person or against the computer. The first player to win 2 out of the 3 rounds will be crowned the winner! Here is some instructions for you to follow. Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard, Lizard poisons Spock, Spock smashes Scissors, Scissors decapitates Lizard, Lizard eats Paper, Paper disproves Spock, Spock vaporizes Rock. Now that has been explained, Enjoy the game!")
        # explain rules    

    # choose game type - Assign a type to Player 2
    def game_mode(self):
        player_response = int(input("Enter 1 to play against another person, or enter 2 to challenge the computer!: "))
        if int(player_response) == 1:
            player_response = self.player_two = Human()
            print(f"You have chosen to play against another Player!")
        elif int(player_response) == 2:
            player_response = self.player_two = AI()
            print(f"You have chosen to play against the Computer!")
        else:
            print("Please select either 1 or 2 to continue!")
        
        # Game round phase - Loop
    def player_picks(self):
        
            self.player_one.choose_gesture()
            self.player_two.choose_gesture()

        # Determine winner of round
    def rule_one(self):
        while self.player_point <=2:
            if self.player_one.choose_gesture == 0  and self.player_two.choose_gesture == 1:
                print("Player one wins") 
                return(self.player_point + 1)
            elif self.player_one.choose_gesture == 1  and self.player_two.choose_gesture == 2:
                print("Player one wins")
                return(self.player_point + 1)
            elif self.player_one.choose_gesture == 2  and self.player_two.choose_gesture == 0:
                print("Player one wins")
                return(self.player_point + 1)
            elif self.player_one.choose_gesture == 0  and self.player_two.choose_gesture == 3:
                print("Player one wins")
                return(self.player_point + 1)       
            elif self.player_one.choose_gesture == 3  and self.player_two.choose_gesture == 4:
                print("Player one wins")
                return(self.player_point + 1)
            elif self.player_one.choose_gesture == 4  and self.player_two.choose_gesture == 1:
                print("Player one wins")
                return(self.player_point + 1)
            elif self.player_one.choose_gesture == 1  and self.player_two.choose_gesture == 3:
                print("Player one wins")
                return(self.player_point + 1)
            elif self.player_one.choose_gesture == 3  and self.player_two.choose_gesture == 2:
                print("Player one wins")
                return(self.player_point + 1)
            elif self.player_one.choose_gesture == 2  and self.player_two.choose_gesture == 4:
                print("Player one wins")
                return(self.player_point + 1)
            elif self.player_one.choose_gesture == 4  and self.player_two.choose_gesture == 0:
                print("Player one wins")
                return(self.player_point + 1)
            elif self.player_one.choose_gesture == self.player_two.choose_gesture:
                print("There has been a tie! Try again.")
                return(self.player_point == 0)
            else:
                print("Player two wins.")
                return(self.player_point +1)
           
        #Determine the winner of the game
    def rule_two(self):    
        player_point = 0
        self.winner_of_game = 2
        if self.player_one == player_point == 2:
            self.player_one = self.winner_of_game
        else:
            self.player_two = self.winner_of_game

        #Endgame
    