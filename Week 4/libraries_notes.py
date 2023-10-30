import random

print(random.random())

# floating point
# starts at 0- doesn't seem to reach 1
# loads of decimal places
# generates a random floating point between 0 and 1. won't ever be number 1 as follow same patten as range.
# probability is between 0 and 1 that's why.

print(random.uniform(1,10))
# missing 2 arguments
# between 1 and 10-Inclusive of both depending on rounding. Floating point and still lots of decimal places

print(random.randint(1,10))
# random whole number(interger)


# randomness- from random library
# my number
# computer number

# while my num doesn't equal computers num
# number don't match

# if my number = computer number
# well done code finished


my_num = 24

rand_num = random.randint(1, 50)

while my_num != rand_num:
    print(f"My number {my_num} does not equal to the randomly generated number {rand_num}")
    rand_num = random.randint(1, 50)

else:
    print(f"The two numbers matched!")

my_num = 24

rand_num = random.randint(1, 50)
counter = 0

while my_num != rand_num:
    print(f"My number {my_num} does not equal to the randomly generated number {rand_num}")
    counter +=1
    rand_num = random.randint(1, 50)

else:
    print(f"The two numbers matched! and it tool {counter+1} times")

# from random import uniform- use this! only import what you need.

# Installing more libraries-pip

# from colorama import Back, Fore, Style
