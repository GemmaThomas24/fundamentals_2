# holiday_items = [
#     "sunscreen",
#     "towel",
#     "towel",
#     "flip flops",
#     "sunglasses",
#     "money",
#     "money",
#     "money"
# ]

# word_search = input("Enter a term to search for  >  ")
# occurrence = holiday_items.count(word_search)
# print(f"The term {word_search}, occurs this many times > {occurrence}")
# list and string method (.count)

# count how many times something apprears in a list- can't use.count- make own .count
# need list of things
# input- what are we searching for?
# counter variable
# need a for loop- for each item in list
# we are telling it to count a specific item.
# for item i'm searching for == item i'm looking at
#  count it - counter +=1


example_list = ["apple", "banana", "orange", "grape", "apple"]

searching_for = input("Enter a term to search for  >  ")

counter = 0 

for i in example_list:
    if  searching_for == i:
        counter +=1

print(f"You searched for {searching_for} and it appeared {counter} times")
# print("You searched for", searching_for, "and it appeared", counter, "times")
# this for loop same as .count- it just shows what is possibly happening behind .count. Saved into a method.