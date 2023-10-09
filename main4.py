# folder application
# so you open a folder which is a container
# could make it so that there is like a set amount of possible folders
# this way i can just make it so each one gets remained with a function like set_folder_name


class Folder:
    def __init__(self, name):
        self.name = name
        self.storage = []

    def display_file_storage(self):
        print("folders:")
        for i in self.storage:
            print(f"- {i.name}")

    def add_file_to_storage(self, folder):
        self.storage.append(folder)


def main_interface(first_folder):
    print("Main Menu")
    print("1. View Folders")
    print("2. Exit Application")
    choice = input("Input: ")
    if choice == "1":
        first_folder.display_file_storage()
        # this line below is cool because it returns the object
        # print(f"{first_folder.storage}")


def storage_application():
    folder_name = input("Please name your first folder's name: ")

    first_folder = Folder(folder_name)
    first_folder.add_file_to_storage(first_folder)
    main_interface(first_folder)


storage_application()
