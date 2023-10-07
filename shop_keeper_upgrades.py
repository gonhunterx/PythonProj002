class ShopKeeper:
    def __init__(self):
        self.shop_inventory = ["Upgrade 1", "Upgrade 2", "Upgrade 3"]
        self.coins = 1000

    def display_inv(self):
        print(f"{self.shop_inventory}")

    # this is going to work by calling the remove from inventory
    # method and this one for now. I will try to combine it later.


class Upgrade:
    def __init__(self, name, value):
        self.name = name
        self.value = value


# creating a dictionary with lists inside it to represent the upgrades?
upgrade_options = {
    "upgrade1": "400",
    "upgrade2": "2000",
    "upgrade3": "5000",
}
# could retrieve this value from the dictionary which can determine the amount to remove from
# player coins. Can do this probably by converting it to a string.


def upgrade_item():
    upgrade = 0

    player_upgrade_option_answer = input("1 or 2: ")
    if player_upgrade_option_answer == "1":
        upgrade += 1


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
            shop(player, shop_keeper)
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
