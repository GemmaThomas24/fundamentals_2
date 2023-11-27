# print("functions notes")
# doesn't have parameters for us to fill in
# .len()- need to put something in brackets for it to work

# def keyword needed to let python know you will be defining a new fundion

# def say_hello():
#     print("Hello")

# say_hello()

# def say_bye():
#     print("Goodbye")

# say_bye()
# ()- telling it to run

# Parameters

# def say_something(something):
#     print(f"{something}")

# say_something("hello there")  - hard coded argument
# say_something(input("what do you want to say?")) sara example- dynamic, user input
# 'hello' is the argument to the parameter 'something'

# def cash_withdrawel (amount, accum):
#     print(f"Withdrawing {amount from account {accum}}")

# balance = 100

# amount = int(input("How much do you want to withdraw?  >  "))

# print(f"You had {balance} and have withdrawn {amount}")

# def cash_withdrawel(amount, accnum):
#     print(f"You have withdrawn {amount} from {accnum}")

# cash_withdrawel(100, 12345678)

# # print(amount)- for example 'amount' only works within the function. When print, 'amount is a varibale not defined on it's own. But within the Function, the paramenter/arugument only exist in that function.

# def coffee_order(size, drink):
#     print(f"You have ordered a {size} size, for a {drink}")

# coffee_order("Large", "Vanilla Latte")

# coffee_order((input("What size coffee do you want to order"")), input("What coffee would you like?"))
# # why do i have to use speech marks for this one and not previous example

# # SCOPE- only exit within the Function

# balance = 1000

# def cash_withdrawel(amount, accnum):
#     global balance
#     print(f"You have {balance}")
#     print(f"You are Withdrawing {amount} from {accnum}")
#     balance = balance - amount
#     print(f"You now have {balance}")

# cash_withdrawel(200, 12345678)


