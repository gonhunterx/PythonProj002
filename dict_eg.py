# Using dictionaries.

my_dictionary = {
    "dog": ["grapes", "chocolate"],
    "cat": ["grapes", "chocolate"],
}
print(type(my_dictionary))

dog_food = my_dictionary["dog"]
cat_food = my_dictionary["cat"]


def food_calculator():
    print("What food would you like to check? ")
    chosen_food = input("Input: ")
    # something to deal with s on the end for consistency

    if chosen_food in dog_food:
        print(f"{chosen_food} is bad for dogs")


# creating input from the user


def main():
    print("Dashpet")
    print("1. Start Program")
    print("2. Quit Program")
    choice = input("Input: ")
    if choice == "1":
        food_calculator()


if __name__ == "__main__":
    main()


# def get_input():
#     look_up = input("Enter ")
