from store import Store
from categories import Categories
from data import categories, products

my_shop = Store("Gio`s Place", categories)

print(my_shop)

my_categories = Categories(products)

print(my_categories)

selection = 0
while selection != len(categories) +1:
    selection = input("Please Select the number of a department. ")
    
    try:
        selection = int(selection)
        if selection == len(categories) + 1:
            print(f"Thanks for shopping at {my_shop.name}")
        elif selection > 0 and selection < len(categories):
            print(categories[selection - 1])
        else:
            print("Please enter valid number")

    except ValueError:
        print("Please enter your choice as a number.")

