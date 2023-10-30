# Activity 1- create a function which takes input of a user's name as a parameter and prints happy birthday song
def happy_birthday(name):
    print(f"Happy birthday to you, happy birthday to you, happy birthday dear {name}, happy birthday to you")

happy_birthday(input("What is your name?"))

# Activity 2

order_count = 0

def take_order(topping, size, crust):
    global order_count
    print("Pizza with {} , a {} size and a {} crust".format(topping, size, crust))
    order_count += 1
    print(order_count)

take_order("Pepperoni", "Medium", "Thick")
take_order("Pepperoni", "Small", "Thick")
take_order("Cheese", "large", "thin")

print(take_order)