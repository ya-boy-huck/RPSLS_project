from player import Player

class Human(Player):
    
    def __init__(self):
        self.choose_gesture()
        super().__init__()
            