import easygui as eg


def welcome():
    while True:
        guide = eg.buttonbox("Welcome to The Takeaway Shop\n"
                             "What would you like to do today", "The Takeaway Shop",
                             choices=["Add or remove a combo", "Find or show combos", "Exit"])
        if guide == "Add or remove a combo":
            add_or_remove()
        elif guide == "Find or show combos":
            find_combo()
        elif guide == "Exit":
            break
        else:
            eg.msgbox("Please choose one of the given options", "Error")


def add_or_remove():
    print("add_combo")


def find_combo():
    print("find_existing_combo")


# Main Routine
welcome()
eg.msgbox("Thanks for using the Takeaway Shop", "Goodbye")

