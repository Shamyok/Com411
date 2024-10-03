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