# Focus on 2 different kinds of loop (for loops and while loops)

# 1. for loops
# list_surroundings = [
#     "water",
#     "monitor",
#     "oranges"
# ]

# print(list_surroundings[2]) ineffiencet - for e.g if you had a list of 1000 things

# list_surroundings = [
#     "water",
#     "monitor",
#     "oranges"
# ]

# for i in list_surroundings:
#     print(i)

# # i runs loop 3 times and prints whole list at same time


# for i in range(5,11):
#     print(i)

# # for i in range(2,12,2):
# #     print(i)
# # # 2,4,6,8,10- step=goes up every 2

# list_of_stuff=["a","b","c","d","e","f"]

# for i in range(5):
#     print(list_of_stuff[i])
# this will print a-e becuase stop number is 4 and in zero index, this is the 5th letter in the sequence

# 2. WHILE LOOP

# answer = input("who ordered a cortado?   >   ")

# while answer != "Alex":
#     print("This is not your drink")
#     answer = input("who ordered a cortado?   >   ")

# else:
#     print("Enjoy yout cortado, Alex")

balance = 100

amount_to_withdraw = int(input("How much do you want to withdraw?  >   "))
while amount_to_withdraw > balance:
    print("insuffucent funds")
    amount_to_withdraw = int(input("How much do you want to withdraw?  >   "))

else:
    balance = balance-amount_to_withdraw
# > the amount is more than balance, so funds insuffienct. Line 53, means that the question, will be asked again. Giving the person another chance to input until correct conditon is met. Allowing us to loop code for an unknown amount of times

# counter = 0 

# while True:
#     counter +=1
#     print(f"This is my {counter} time looping")






