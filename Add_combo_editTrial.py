# Adding an option to edit combo after creation
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
            menu[new_combo]["Total cost"] = sum([side[1], drink[1], burger[1]])
            redo = ""
            while redo != "Perfect":
                print(menu[new_combo])
                redo = eg.buttonbox("Is this correct or would you like to change an item",
                                    "Change combo", choices=["Burger", "Drink", "Side", "Perfect"])
                change = eg.enterbox(f"{redo}", f"{redo} choice"), eg.integerbox("Price:", f"{redo} price")
                menu[new_combo][redo] = change
                menu[new_combo]["Total cost"] = sum([side[1], drink[1], burger[1]])
        elif add_remove == "Remove combo":
            combo_removed = eg.buttonbox("Which combo would you like to remove from the menu", "Remove combo",
                                         choices=combo_names)
            if menu.get(combo_removed):
                del menu[combo_removed]
                combo_names.remove(combo_removed)
            else:
                eg.msgbox("Returning", "Return")


# Main Routine
add_or_remove()
