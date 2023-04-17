import easygui as eg

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
combo_names = ["Return", "Value", "Cheezy", "Super"]


def add_or_remove():
    add_remove = ""
    while add_remove != "Quit":
        add_remove = eg.buttonbox("Would you like to add a combo remove a combo or quit", "Combos",
                                  choices=["Add combo", "Remove combo", "Quit"])
        if add_remove == "Add combo":
            new_combo = eg.enterbox("Enter the combo name", "Combo name")
            combo_names.append(new_combo)
            menu[new_combo] = {}
            burger = [eg.enterbox("Burger:", "Burger choice"), eg.integerbox("Price:", "Burger price")]
            menu[new_combo]["Burger"] = burger
            drink = [eg.enterbox("Drink:", "Drink choice"), eg.integerbox("Price:", "Drink price")]
            menu[new_combo]["Drink"] = drink
            side = [eg.enterbox("Side:", "Side choice"), eg.integerbox("Price:", "Side price")]
            menu[new_combo]["Side"] = side
            menu[new_combo]["Total Cost"] = sum([side[1], drink[1], burger[1]])
        elif add_remove == "Remove combo":
            combo_removed = eg.buttonbox("Which combo would you like to remove from the menu", "Remove combo",
                                         choices=combo_names)
            if menu.get(combo_removed):
                del menu[combo_removed]
                combo_names.remove(combo_removed)
            else:
                eg.msgbox("This combo is not on the menu", "Unlisted combo")


def find_combo():
    find_show = ""
    while find_show != "Exit":
        find_show = eg.buttonbox("Would you like to find a combo, show the menu or exit", "Pathway",
                                 choices=["Find combo", "Show menu", "Exit"])
        if find_show == "Find combo":
            combo_find = eg.buttonbox("Which combo would you like to find", "Combo directory", choices=combo_names)
            if combo_find == "Return":
                break
            else:
                combo = menu.get(combo_find)
                print(combo)
        elif find_show == "Show menu":
            for food, name in menu.items():
                print(f"{food}, {name}")


# Main Routine
find_combo()
