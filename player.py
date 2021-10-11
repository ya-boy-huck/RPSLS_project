class Player:

    def __init__(self):
        self.rules = ""
        self.gesture = ["Rock", "Scissors", "Paper" , "Lizard", "Spock"]
        self.gesture_choice = []
    
    def gesture(self):
        while True:
            self.gesture = input("Enter 0 for Rock, 1 for Scissors, 2 for Paper, 3 for Lizard, 4 for Spock")
           
            if self.gesture.lower() not in ('0','1', '2', '3', '4'):
                     print("Please try again and Enter 0 for Rock, 1 for Scissors, 2 for Paper, 3 for Lizard, 4 for Spock")
            else:
                break

            if self.gesture == "0":
                print(f"You have chosen {self.gesture[0]}")
            if self.gesture == "1":
                print(f"You have chosen {self.gesture[1]}")
            if self.gesture == "2": 
                print(f"You have chosen {self.gesture[2]}")
            if self.gesture == "3":        
                print(f"You have chosen {self.gesture[3]}")
            if self.gesture == "4":
                print(f"You have chosen {self.gesture[4]}")
            else:
                print("That is not a valid entry, please try again")

    
    def rules(self):
        for gestures in self.gestures:
           if [0] < [1]:
               player_point += 1
           elif [1] < [2]:
               player_point += 1
           elif [2] < [0]: 
               player_point += 1
           elif [0] < [3]: 
               player_point += 1
           elif [3] < [4]: 
               player_point += 1
           elif [4] < [1]: 
               player_point += 1
           elif [1] < [3]:
               player_point += 1
           else:
               gesture == gesture
        pass
