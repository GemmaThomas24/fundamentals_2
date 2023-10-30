# Activity 1
favourite_websites = [
    "youtube",
    "netflix",
    "asos"
]

print(favourite_websites)

favourite_websites.append("lookfantastic")
favourite_websites.append("ohpolly")

print(favourite_websites)

favourite_websites.pop()

print(favourite_websites)

# using .append twice (or however many times you like), will keep adding to your list
# .pop will remove the last website on the list

# Activity 2

shopping_list = [
    "apple",
    "carrot",
    "pizza",
    "carrot",
    "dog food",
    "orange juice",
    "egg",
    "kale",
    "carrot",
    "kale",
    "orange juice",
    "kale",
    "toilet roll",
    "stamps",
    "noodles",
    "pasta sauce",
    "egg",
    "pasta sauce"
]

print(shopping_list.count("egg"))
print(shopping_list.count("kale"))
print(shopping_list.count("stamps"))
print(shopping_list.count("carrot"))
print(shopping_list.count("orange juice"))

# Activity 3
# write programme demonstrating each list method

holiday_items = [
    "sunscreen",
    "towel",
    "flip flops",
    "sunglasses",
    "money"
]

holiday_items.remove("towel")
print(holiday_items)
# .remove = removes whatever item you state within the brackets. You can't leave this blank, must state 1 argument.

holiday_items = [
    "sunscreen",
    "towel",
    "flip flops",
    "sunglasses",
    "money"
]

holiday_items.reverse()
print(holiday_items)
# don't need to input anything within the brackets. The method .reverse will automatically reverse the order of the list

holiday_items = [
    "sunscreen",
    "towel",
    "flip flops",
    "sunglasses",
    "money"
]

holiday_items.sort(reverse=True)
print(holiday_items)
# .reverse=True (goes in desencding order - for e.g from Z-A of the alphabet)

def myFunc(e):
    return len(e)

holiday_items = [
    "sunscreen",
    "towel",
    "flip flops",
    "sunglasses",
    "money"
]

holiday_items.sort(key=myFunc)
print(holiday_items)

# Sorts the list by the length of the values

holiday_items = [
    "sunscreen",
    "towel",
    "flip flops",
    "sunglasses",
    "money",
    "money"
]

print(holiday_items.count("money"))
# when printed in terminal, should receive back the number 2 as money is there twice. Method .count, counts how many times a value appears in the list.

holiday_items = [
    "sunscreen",
    "towel",
    "flip flops",
    "sunglasses",
    "money"
]

extra_items = ["clothes" , "book"]

holiday_items.extend(extra_items)

print(holiday_items)
# You need to create a variable for the Extra Items (Extra_Items). I've assigned Clothes and Book to this variable. On line 128, code tells the holiday_item variable to extend the list with the extra_item variable.
# Once this is done, you print holiday_items again, and outcome should include the 2 extra items. 







