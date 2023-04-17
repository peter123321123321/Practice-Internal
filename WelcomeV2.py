import easygui as eg


def welcome():
    guide = eg.buttonbox("Welcome to The Takeaway Shop\n"
                         "What would you like to do today", "The Takeaway Shop",
                         choices=["Add a combo", "Find an existing combo", "Delete a combo", "Show the menu", "Exit"])
    function = {"Add a combo": add_combo,
                "Find an existing combo": find_existing_combo,
                "Delete a combo": delete_combo,
                "Show the menu": show_menu,
                "Exit": exit_program}
    chosen_function = function.get(guide)
    chosen_function()


def add_combo():
    print("add_combo")


def find_existing_combo():
    print("find_existing_combo")


def delete_combo():
    print("delete_combo")


def show_menu():
    print("show_menu")


def exit_program():
    print("exit_program")


# Main Routine
welcome()
