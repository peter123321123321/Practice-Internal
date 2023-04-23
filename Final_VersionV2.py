import easygui as eg

# Dictionary containing all the combos both original and user added
menu = {"Value": {"Burger": ["Beef burger", 5.69],
                  "Drink": ["Fries", 1],
                  "Side": ["Fizzy drink", 1],
                  "Total cost": 7.69},
        "Cheezy": {"Burger": ["Cheeseburger", 6.69],
                   "Drink": ["Fries", 1],
                   "Side": ["Fizzy drink", 1],
                   "Total cost": 8.69},
        "Super": {"Burger": ["Cheeseburger", 6.69],
                  "Drink": ["Large fries", 2],
                  "Side": ["Smoothie", 2],
                  "Total cost": 10.69}}
# List containing the names of all the added combos as well as a return option for easygui button boxes
combo_names = ["Return", "Value", "Cheezy", "Super"]


def welcome():
    # While true statement loops function
    while True:
        # Ask user what they'd like to do using button box
        guide = eg.buttonbox("Welcome to The Takeaway Shop\n"
                             "What would you like to do today", "The Takeaway Shop",
                             choices=["Add or remove a combo", "Find or show combos", "Exit"])
        # Depending on what button they chose they'll be routed to a different function,
        # or it'll break the loop and exit
        if guide == "Exit":
            break
        function = {"Add or remove a combo": add_or_remove,
                    "Find or show combos": find_combo}
        chosen_function = function.get(guide)
        chosen_function()


def add_or_remove():
    # Loops function till the user chooses Return
    add_remove = ""
    while add_remove != "Return":
        # Lets user choose whether they want to add combo, remove combo or return using if statements
        add_remove = eg.buttonbox("Would you like to add a combo remove a combo or Return", "Combos",
                                  choices=["Add combo", "Remove combo", "Return"])
        if add_remove == "Add combo":
            # Asks for the combo names and combo item and price then adds it to the dictionary and adds the sum of all
            # The items as well as adds name to the list
            new_combo = eg.enterbox("Enter the combo name", "Combo name")
            combo_names.append(new_combo)
            menu[new_combo] = {}
            burger = [eg.enterbox("Burger:", "Burger choice"), eg.integerbox("Price:", "Burger price")]
            drink = [eg.enterbox("Drink:", "Drink choice"), eg.integerbox("Price:", "Drink price")]
            side = [eg.enterbox("Side:", "Side choice"), eg.integerbox("Price:", "Side price")]
            menu[new_combo]["Burger"] = burger
            menu[new_combo]["Drink"] = drink
            menu[new_combo]["Side"] = side
            menu[new_combo]["Total cost"] = sum([side[1], drink[1], burger[1]])
            # Loops function until the user decides that the combo has no errors and chooses perfect
            while True:
                # Prints new combo
                print(menu[new_combo])
                # Asks user what combo they'd like to change breaks loop if its perfect
                redo = eg.buttonbox("Is this correct or would you like to change an item",
                                    "Change combo", choices=["Burger", "Drink", "Side", "Perfect"])
                if redo == "Perfect":
                    break
                # Changes the item that was chosen in redo, Changes dictionary value than adds the price together
                change = eg.enterbox(f"{redo}", f"{redo} choice"), eg.integerbox("Price:", f"{redo} price")
                menu[new_combo][redo] = change
                menu[new_combo]["Total cost"] = sum([side[1], drink[1], burger[1]])
        elif add_remove == "Remove combo":
            # If the user wants to remove a combo it'll ask them which one then search for that combo in the dictionary
            # And list and remove them
            combo_removed = eg.buttonbox("Which combo would you like to remove from the menu", "Remove combo",
                                         choices=combo_names)
            if menu.get(combo_removed):
                del menu[combo_removed]
                combo_names.remove(combo_removed)
            else:
                eg.msgbox("Returning", "Return")


def find_combo():
    # Loops function until they choose to return
    find_show = ""
    while find_show != "Return":
        # Asks them what they would like to do and use if statements
        find_show = eg.buttonbox("Would you like to find/edit a combo, show the menu or Return", "Pathway",
                                 choices=["Find/edit combo", "Show menu", "Return"])
        if find_show == "Find/edit combo":
            combo_find = eg.buttonbox("Which combo would you like to find/edit", "Combo directory", choices=combo_names)
            if combo_find == "Return":
                break
            else:
                # Loops until the combos perfect
                redo = ""
                while redo != "Perfect":
                    # Prints the combo the user wanted to find then asks them if they want to change anything
                    combo = menu.get(combo_find)
                    print(combo_find, combo)
                    redo = eg.buttonbox("Is this correct or would you like to change an item",
                                        "Change combo", choices=["Burger", "Drink", "Side", "Perfect"])
                    # Asks for the names and price then changes it in the dictionary and adds the sum of all the items
                    if redo == "Burger":
                        burger1 = [eg.enterbox("Burger:", "Burger choice"), eg.integerbox("Price:", "Burger price")]
                        menu[combo_find]["Burger"] = burger1
                    elif redo == "Drink":
                        drink1 = [eg.enterbox("Drink:", "Drink choice"), eg.integerbox("Price:", "Drink price")]
                        menu[combo_find]["Drink"] = drink1
                    elif redo == "Side":
                        side1 = [eg.enterbox("Side:", "Side choice"), eg.integerbox("Price:", "Side price")]
                        menu[combo_find]["Side"] = side1
                    menu[combo_find]["Total cost"] = sum([menu[combo_find]["Burger"][1], menu[combo_find]["Drink"][1],
                                                          menu[combo_find]["Side"][1]])

        elif find_show == "Show menu":
            # Prints all combos as well as their names to the user
            for food, name in menu.items():
                print(f"{food}, {name}")


# Main Routine
welcome()
