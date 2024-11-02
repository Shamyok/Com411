def directions():
    steps: list = ["Move forward", "Move backward", "Turn left", "Turn right"]
    return steps

def run_task1():
    directions()

def movements():
    path = ["Move Forward", 10, "Move backward", 5,"Move Left",3, "Move Right", 1]
    return path

def run_task2():
    print("Moving...")
    movements1 = movements()
    for i in range(0, len(movements1), 2):
        print(f"{movements1[i]} for {movements1[i+1]}")

def menu():
    print("Please select a direction")
    direction_list = directions()
    for i in range(len(direction_list)):
        direction = direction_list[i]
        print(f"{i}: {direction}")

def run_task3():
    menu()

run_task3()
