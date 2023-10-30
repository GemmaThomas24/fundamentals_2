#Activity 1
user_name = input("what is your name?")

user_age = input(" How old are you?")

favourite_colour = input(" What is your favourite colour?")

print(f"My name is {user_name}, I am {user_age} years old, and my favourite colour is {favourite_colour}")

# # user_name = input("what is your name?")
# # print(f"My name is {user_name}")

# # user_age = input(" How old are you?")
# # print(f"I am {user_age} years old")

# # favourite_colour = input(" What is your favourite colour?")
# # print(f" My favourite colour is {favourite_colour}")


# #Activity 2
# #casting
print("Type in two numbers to multiply them")

num1 = int(input("Number 1:   >   "))
num2 = int(input("Number 2:   >   "))

print(num1*num2)
print(num1+num2)
print(num1-num2)
print(num1/num2)
print(num1**num2)
print(num1%num2)

#Activity 3
cost_per_apple = 0.25

num1 = int(input("How many apples would you like to purchase? > "))

total_cost = num1 * cost_per_apple

pounds = int(total_cost)
pence = int((total_cost - pounds) * 100)

print(f"The total cost is {pounds} pounds and {pence} pence.")
# the first half I was able to figure out, but after total_cost = num1 * cost_per_apple, I used google for help as I couldn't figure out how to 
# make it print in pounds and pence.
# Pounds = int - if the total cost is 1.25, the 'int' isolates the number 1 (the interger).
# Then for Pence, you take away 1.25- 1 (anything after the decimal is not counted), you're left with 0.25, times
# this by 100 gives you the Pence 25p