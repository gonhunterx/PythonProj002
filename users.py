class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


def login_screen(login_info):
    print("Please enter your login information.")
    entered_username = input("Username: ")
    entered_password = input("Password: ")
    try_login_info = [entered_username, entered_password]
    if try_login_info == login_info:
        print("yay!")
        main()
    else:
        print("Incorrect information.")


def intro_statement():
    print("Welcome to LamaMage: LamaForge's Custom File System")
    print("Please create an account ^-^!")
    username = input("Enter a Username: ")
    password = input("Enter a Password: ")
    login_info = User(username, password)
    print("Do you want to review your login information before entering?")
    info_answer = input("yes or no: ")
    if info_answer.lower() == "yes":
        print([f"Login Info: User: {username}, PW: {password}"])
    else:
        print("You continue.")
    return login_info


def main():
    login_info = intro_statement()

    login_screen(login_info)


if __name__ == "__main__":
    main()
