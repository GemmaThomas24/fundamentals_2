# General re-cap
# While Loop
# actual password
# password user types in
# == want if actual password equals password user types in:
# allowed in the account
# while the password don't match:
# tell them they don't match and ask for password again


# password = "12345678"
# user_password = input("What is your password?")

# while password != user_password:
#     print(Incorrect!)
#     user_password = input("What is your password?")

# else:
#     print("Welcome to your account")

password = "12345678"
user_password = input("What is your password?")
attempts = 1

while password != user_password and attempts <3:
    # loop will break under 2 conditons
    # lopp will break is password is right or attempts go beyond 3.
    print("Incorrect!")
    # attempts +=1 
    attempts = attempts +1
    user_password = input("What is your password?")
else:
    if password == user_password:
        print("Welcome to your account")
    else:
        print("Locked out")

# while the password is wrong and they still have enough attempts to try again
# use counter


# Palindrome Activity

print("hello"[2])





# project.py
import random
from colorama import Fore
# virtual environment
# from colorama import Back, Fore, Style

# what we going to need for Magic 8
# need Random Library- is importable
# need colourama- installable library- from the internet
# List of good responses and list of bad responses 
# input- whar is your question?
# background, generate random number
# odd-bad fortune
# even- good fortune
# if number % 2== 0 -> good fortune -> randomly pick from good list
# if odd number -> bad fortune -> randomly pick from bad ist

good_fortunes = [
    "yes",
    "It seems so",
    "I see good signs"
]

bad_fortunes = [
    "No",
    "It seems not",
    "I think so",
    "Deffo not"
]

input("Ask the magic 8 ball a yes or no question    >   ")
rand_num = random.randint(1,10)
print(rand_num)

if rand_num %2 == 0:
    print(Fore.GREEN + random.choice(good_fortunes))
    # print(good_fortunes[random.randint(0,2)])
else:
    print(Fore.RED + random.choice(bad_fortunes))
    # print(bad_fortunes[random.randint(0,len(bad_fortunes)-1)])
