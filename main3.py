import sys


# class IronOre:
#     def __init__(self):
#         self.name = "iron ore"


def mines(player):
    print("You enter the mines.")
    mine_or_leave = input("Do you want to mine or go back?(1 or 2): ")
    if mine_or_leave == "1":
        # creating a var that acts as the IronOre class
        iron_ore = Item("iron ore", 5)
        player.add_to_inventory(iron_ore)
        print("You have obtained an iron ore!")
        mines(player)
    elif mine_or_leave != "1":
        menu(player)


class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value


# # defining a class for wood logs
# class WoodLog:
#     def __init__(self):
#         self.name = "wood log"

# defining items: idk if this is necessary but i think its probaby fine to have until its too large.
iron_ore = Item("iron ore", 5)
wood_log = Item("wood log", 4)


def woods(player):
    print("You enter the woods.")
    cut_or_leave = input("Do you want to cut wood or go back?(1 or 2): ")
    if cut_or_leave == "1":
        wood_log = Item("wood log", 4)
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
            print([item.name])  # displaying the name of the items
        print(f"Coins: {self.coins}")

    # appending items to the players storage
    def add_to_inventory(self, item):
        self.storage.append(item)

    # creating a remove from inv because that is just how we will handling selling items for now
    # def remove_from_inventory(self, item):
    #     # right now i think this just sells the top item in the list
    #     self.storage.pop(item)
    # remaking it
    def remove_first_item_from_inventory(self):
        if self.storage:  # checking if the inventory is empty
            removed_item = self.storage.pop(0)  # remove and return the first item
            return removed_item
        else:
            return None  # Inventory is empty


class ShopKeeper:
    def __init__(self):
        self.shop_inventory = ["Upgrade 1", "Upgrade 2", "Upgrade 3"]
        self.coins = 1000

    def display_inv(self):
        print(f"{self.shop_inventory}")

    # this is going to work by calling the remove from inventory
    # method and this one for now. I will try to combine it later.


def buy_item_from_player(player):
    # item at the top of the players inventory
    # have to get that somehow
    # for item in len(player.storage):
    #     print(item)
    if wood_log in player.storage:
        player.coins += 4
    else:
        player.coins += 5
    return player
    # # item_player_is_selling = player.storage[0]
    # if item_player_is_selling == wood_log:
    #     player.coins += 4
    # else:
    #     player.coins += 5
    # return player


def shop_menu():
    print("you enter the shop and walk to the counter...")
    print("SHOP MENU:")
    print("1. Buy")
    print("2. Sell")
    print("3. Exit Shop")


def shop(player, shop_keeper):
    shop_menu()
    shop_keeper = ShopKeeper()
    shop_choice = input("Input: ")
    if shop_choice == "1":
        # more logic about the options
        # renamed the ShopKeeper class to shop_keeper and are now calling the display_inv method
        shop_keeper.display_inv()
        # for now we are not doing anything here just going to work on the sell function
        shop_buy_menu_choice = input("1 to continue...")
        if shop_buy_menu_choice == "1":
            menu(player)
        else:
            print("press 1 to continue.")
    elif shop_choice == "2":
        buy_item_from_player(player)
        removed_item = player.remove_first_item_from_inventory()
        if removed_item:
            # shop_keeper.add_item_to_shop(removed_item)
            player.coins += removed_item.value
            print(f"You sold {removed_item.name}")
            shop(player, shop_keeper)
        else:
            print("Your inventory is empty.")
            shop(player, shop_keeper)
    elif shop_choice == "3":
        print("Invalid choice.")
        menu(player)


def menu(player):
    print("=================")
    print("Main Menu:")
    print("1. Go to mines")
    print("2. Go to the woods")
    print("3. View Inventory")
    print("4. Go to the shop")
    print("5. Exit Game")
    shop_keeper = ShopKeeper()
    menu_choice = input("Input: ")
    if menu_choice == "1":
        mines(player)
    elif menu_choice == "2":
        woods(player)
    elif menu_choice == "3":
        player.display_inventory()
        menu(player)
    elif menu_choice == "4":
        shop(player, shop_keeper)
    elif menu_choice == "5":
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

    # shop(shop_keeper)
    menu(player)


if __name__ == "__main__":
    main()
