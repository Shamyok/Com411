print("What type of book is this?")
book = input().lower()

if book == "adventure":
    print("I like adventure books!")

print ("Finished reading book")

print ("Please enter the activity to be performed.")
activity = input().lower()

if activity == "calculate":
    print("Performing calculations...")
else:
    print("Performing activity...")

print("Activity completed!")

print("Towards which direction should I go (up, down ,left or right) up?")
direction = input().lower()

if direction == "up":
    print("I am moving in an upwards direction!")
elif direction == "down":
    print("I am moving in an downwards direction!")
elif direction == "left":
    print("I am moving to the left!")
elif direction == "right":
    print("I am moving to the right!")

print("Please enter a whole number")
number = int(input())

if (number%2==0):
    print("The number is even")
else:
    print("The number is odd")

print("Please enter the first number")
number1 = int(input())
print("Please enter the second number")
number2 = int(input())
if (number1==number2):
    print("The numbers are equal")
elif (number1>number2):
    print("The first number is greater than the second number")
else:
    print("The second number is greater than the first number")


print("Please enter the first whole number")
odd = 0
even = 0
wholenum = int(input())
if (wholenum%2==0):
    even += 1
else:
    odd += 1
print("Please enter the second whole number")
wholenum2 = int(input())
if (wholenum2%2==0):
    even += 1
else:
    odd += 1
print("Please enter the third whole number")
wholenum3 = int(input())
if (wholenum3%2==0):
    even += 1
else:
    odd += 1
print(f"There was {even} even and {odd} odd numbers")

