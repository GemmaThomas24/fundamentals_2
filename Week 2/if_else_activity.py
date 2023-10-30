# Activity 1

password = "codenation123"

if len(password) < 8:
    print("The password is too short.")

else:
    print(password)

# # Activity 2

num = 15

if num % 3 == 0 or num % 5 == 0:
    print("This number is divisible by 3 or 5")
else:
    print("This number is not divisible by 3 or 5")
# using 15 as an example, there is no remainder when divided by 3 or 5, therefore answer is 0(Modulo). Meaning it is divisable by 3 or 5.
# using 'or' logical operator. meaning only one has to be true to print sentence. If both not True, it will print the 'else'

# Activity 3

num = 21

if num % 3 == 0 and num % 7 == 0:
    print("fizzbuzz")
elif num % 3 == 0:
    print("fizz")
elif num % 7 == 0:
    print("buzz")
else:
    print(num)

# same reasoning as above but with more conditons ('elif'). Instead of using logiical operator 'or', we use 'and' as we need both to be true, to call it Fizzbuzz

# Activity 4

print("What is the captial of England?")

answer = input("Type your answer here  > ")

if answer == "London":
    print("Correct! The answer is London")
elif answer == "london":
    print("Correct! The answer is london")
else:
    print(f"Incorrect, the answer is 'London', not {answer}")

# Activity 5
# create a variable called word that takes a string.
# create an if statement that checks if the last letter is the same as the first.
# if it is return true, otherwise return false

word = "pop"

if word[0] == word[-1]:
    print("True")

else:
    print("False")
# Python is Zero index based: 1st character in string has index of 0. using [-1] refers to last character of string (negative indexing)
# the code is saying, if Word[0] 1st character letter is equal(same as), [-1] the last character: produce True.