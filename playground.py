class Weapon:
    def __init__(self, name, damage, price):
        self.name = name
        self.damage = damage
        self.price = price


class Player:
    def __init__(self, name):
        self.name = name
        # right now the first item in the inv is always going to be the weapo
        self.inventory = []
        self.coins = 0
        # however, you could make it so that there is a weapon slot specifically.

    def display_stats(self):
        print(f"{self.name}")
        for item in self.inventory:
            print(item.name)
        print(f"{self.coins}")


def battle_sequence(player):
    # something like we need to check what item the player picked so like
    # append the item to the players inventory and then check that?
    # idk
    pass


def shop(player):
    pass


def intro_function(player):
    return player
    pass


def main():
    print("welcome to namatoki nato")
    battle_axe = Weapon("Battle Axe", 6, 15)
    short_sword = Weapon("Short Sword", 3, 10)
    dagger = Weapon("Dagger", 4, 13)

    player_name = input("What is your name?: ")
    player = Player(player_name)
    weapon_choice = input("Battle Axe, Short Sword, or Dagger: ")
    if weapon_choice.lower() == "battle axe":
        player.inventory.append(battle_axe.name)
    elif weapon_choice.lower() == "short sword":
        player.inventory.append(short_sword.name)
    elif weapon_choice.lower() == "dagger":
        player.inventory.append(dagger.name)
    print(player.inventory)
    # weapon_choice = input("Which weapon do you choose?: ")

    intro_function(player)


if __name__ == "__main__":
    main()
