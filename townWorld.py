import sys


class Player:
    def __init__(self, name):
        self.name = name
        self.money = 0


class MoneyHouse:
    def __init__(self, production_rate):
        self.production_rate = production_rate

    def generate_revenue(self, rate):
        self.production_rate += rate


def scary_temple(player):
    # a place where the player can get money to upgrade generation rate
    print("You enter the scary temple...")
    first_decision = input("Stay or Leave: ")
    if first_decision.lower() == "stay":
        print("You will be rewarded for your decision.")
        print("A monster flies out of bush and attacks you!")
        attack_or_run = input("Do a flip and kick it back or run. 1 or 2: ")
        if attack_or_run == "1":
            player.coins += 5
            return player
        else:
            print("you have died...")
            sys.exit()
    pass

def shop(player, generation_rate):
    



def battle_sequence(player):
    pass


def main():
    player_name = input("What is your name?: ")
    player = Player(player_name)

    rate = 2
    generation_rate = MoneyHouse(rate)
    # menu
    print("Main menu:")
    print("1. Temple")
    print("2. Shop")
    print("3. Quit")
    choice = input("input: ")
    if choice == "1":
        scary_temple(player)
    elif choice == "2":
        shop(player, generation_rate = 1)
    elif choice == "3":
        sys.exit()
