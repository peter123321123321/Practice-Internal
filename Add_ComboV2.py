# changed the prices to integers and enter-boxes to integers so that you can find the total cost of each combo
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


def add_or_remove():
    add_remove = eg.buttonbox("Would you like to add or remove a combo", "Combos",
                              choices=["Add combo", "Remove combo"])
    if add_remove == "Add combo":
        new_combo = eg.enterbox("Enter the combo name", "Combo name")
        menu[new_combo] = {}
        burger = [eg.enterbox("Burger:", "Burger choice"), eg.integerbox("Price:", "Burger price")]
        menu[new_combo]["Burger"] = burger
        drink = [eg.enterbox("Drink:", "Drink choice"), eg.integerbox("Price:", "Drink price")]
        menu[new_combo]["Drink"] = drink
        side = [eg.enterbox("Side:", "Side choice"), eg.integerbox("Price:", "Side price")]
        menu[new_combo]["Side"] = side
        menu[new_combo]["Total Cost"] = sum([side[1], drink[1], burger[1]])
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
