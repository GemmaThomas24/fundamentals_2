# Activity 1- create a loop that prints "hello world" 13 times. Then convert this into a while look that does the same job.

for i in range(13):
    print("Hello World")

# counter = 0

# while counter <= 13:
#     print("Hello World")
#     counter +=1

# Not sure how to create this into a While Loop?

# # Activity 2- use a nested for loop to write a programme which prints out multiplication tables from 1 to 12

for i in range(1, 13):
    # print("\n")- looked online and found this is used to create a break in nested loops. Can also use print()
    for j in range(1, 13):
        print(i * j)

# if you left code as 'for in in range(1,13)'. it will print out 1-12. So below you need an inner loop with the same range
# and times them together. 1(i)x 1(j) , 1(i) x 2(j) and so on. 

# # Activity 3

password = input("Please enter your password:   ")
password_attempt = 3 

while password == "codenation1234":
    print("Welcome to your account")
    password = input("Please enter your password:   ")
else:
    print("Your password is incorrect, please try again")  
    
#Not sure how to incorperate the password attempt into the code. Doesn't seem to promt me to type in the password again.