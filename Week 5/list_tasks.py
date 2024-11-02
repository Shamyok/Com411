def directions():
    print(list(["Move forward", "Move backward", "Turn left", "Turn right"]))

path = ["Move forward", 10, "Move backward", 5 , "Move Left", 3 , "Move Right", 1]
print("Moving...")
for i in range(0, len(path), 2):
    print(f"{path[i]} for {path[i+1]}")


steps = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]

def menu():
    print("Please select a direction:")
    for i in range(len(steps)):
        print(f"{i}: {steps[i]}")

def menu_and_input():
    print("Please select a direction:")
    for i in range(len(steps)):
        print(f"{i}: {steps[i]}")
    escape = input()
menu_and_input()






