class Player:
    def __init__(self, name):
        self.name = name
        self.coins = 0 
        self.experience = 0
    
    def displayStats(self):
        print({self.name})
        print({self.coins})
        print({self.experience})        
        
def main():
    print("welcome to paradise")
    player_name = input("What is your name?: ")
    # player = player with the input name as one of the attributes
    player = Player(player_name)
    
    print("1. Display stats")
    print("2. Quit game")
    print("3. Continue...")
    player_choice = input("What is your choice?: ")
    if player_choice = "1":
        player = displayStats(player)
        
    
    