class Player:

    def __init__(self): 
        self.gesture = ["Rock", "Scissors", "Paper" , "Lizard", "Spock"]
        self.player_point = 0
        

    def choose_gesture(self):
     while True:
        self.gesture_choice = input("Enter 0 for Rock, 1 for Scissors, 2 for Paper, 3 for Lizard, 4 for Spock: ")
        if self.gesture_choice == "0":
            print(f"You have chosen {self.gesture[0]}")
        elif self.gesture_choice == "1":
            print(f"You have chosen {self.gesture[1]}")
        elif self.gesture_choice == "2": 
            print(f"You have chosen {self.gesture[2]}")
        elif self.gesture_choice == "3":        
            print(f"You have chosen {self.gesture[3]}")
        elif self.gesture_choice == "4":        
            print(f"You have chosen {self.gesture[4]}")
        if self.gesture_choice not in ['0','1', '2', '3', '4']:
                     print("Please try again and Enter 0 for Rock, 1 for Scissors, 2 for Paper, 3 for Lizard, 4 for Spock: ")
        else:
            break