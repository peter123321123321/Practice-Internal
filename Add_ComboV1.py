import easygui as eg


def add_or_remove():
    menu = {"Value": {"Burger": ["Beef burger", "5.69"],
                      "Drink": ["Fries", "1"],
                      "Side": ["Fizzy drink", "1"]},
            "Cheezy": {"Burger": ["Cheeseburger", "6.69"],
                       "Drink": ["Fries", "1"],
                       "Side": ["Fizzy drink", "1"]},
            "Super": {"Burger": ["Cheeseburger", "6.69"],
                      "Drink": ["Large fries", "2"],
                      "Side": ["Smoothie", "2"]}}
    add_remove = eg.buttonbox("Would you like to add or remove a combo", "Combos",
                              choices=["Add combo", "Remove combo"])
    if add_remove == "Add combo":
        new_combo = eg.enterbox("Enter the combo name", "Combo name")
        menu[new_combo] = {}
        burger = [eg.enterbox("Burger:", "Burger choice"), eg.enterbox("Price:", "Burger price")]
        menu[new_combo]["Burger"] = burger
        drink = [eg.enterbox("Drink:", "Drink choice"), eg.enterbox("Price:", "Drink price")]
        menu[new_combo]["Drink"] = drink
        side = [eg.enterbox("Side:", "Side choice"), eg.enterbox("Price:", "Side price")]
        menu[new_combo]["Side"] = side
        for food, name in menu.items():
            print(f"{food}, {name}")
    elif add_remove == "Remove combo":
        combo_removed = eg.enterbox("Which combo would you like to remove from the menu", "Remove combo")
        if menu.get(combo_removed):
            menu.pop(combo_removed)
        else:
            eg.msgbox("This combo is not on the menu", "Unlisted combo")


# Main Routine
add_or_remove()
