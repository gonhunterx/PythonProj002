import sys


class IronOre:
    def __init__(self):
        self.name = "iron ore"


def mines(player):
    print("You enter the mines.")
    mine_or_leave = input("Do you want to mine or go back?(1 or 2): ")
    if mine_or_leave == "1":
        # creating a var that acts as the IronOre class
        iron_ore = IronOre()
        player.add_to_inventory(iron_ore)
        print("You have obtained an iron ore!")
        mines(player)
    elif mine_or_leave != "1":
        menu(player)


# defining a class for wood logs
class WoodLog:
    def __init__(self):
        self.name = "wood log"


def woods(player):
    print("You enter the woods.")
    cut_or_leave = input("Do you want to cut wood or go back?(1 or 2): ")
    if cut_or_leave == "1":
        wood_log = WoodLog()
        player.add_to_inventory(wood_log)
        print("You have obtained a wood log!")
        woods(player)
    elif cut_or_leave != "1":
        menu(player)


class Player:
    def __init__(self, name):
        self.name = name
        self.storage = []
        self.coins = 0

    def display_inventory(self):
        print(f"Username: {self.name}")
        print("Inventory:")
        for item in self.storage:
            print(item)  # displaying the name of the items
        print(f"Coins: {self.coins}")

    # appending items to the players storage
    def add_to_inventory(self, item):
        self.storage.append(item)


class Shop:
    def __init__(self):
        self.sell = 10


def menu(player):
    print("Main Menu:")
    print("1. Go to mines")
    print("2. Go to the woods")
    print("3. View Inventory")
    print("4. Exit Game")
    menu_choice = input("Input: ")
    if menu_choice == "1":
        mines(player)
    elif menu_choice == "2":
        woods(player)
    elif menu_choice == "3":
        player.display_inventory()
    elif menu_choice == "4":
        sys.exit()
    else:
        print("Invalid Choice. Please select a menu option.")


def get_player_name():
    player_name = input("What is your name?: ")
    return player_name


def main():
    # creating a player_name var to get the input of the player with the get player name func
    player_name = get_player_name()
    # make a var that passes the input from player_name into the Player class in the name position
    player = Player(player_name)
    # using a loop to initiate the players instance into the menu.
    menu(player)


if __name__ == "__main__":
    main()
