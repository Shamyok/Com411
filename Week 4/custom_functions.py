def listen():
    sound = input("What sound did you hear?")
    print(f"That was a loud {sound}!")



def identify():
    reponse = input("What lies before us?")
    if reponse.lower() == "a large boulder":
        print("Its time to run!")
    else:
        print("We will be fine.")


def escape_by(plan):
    if plan == "jumping over":
        print("We cannot esacpe that way! The boulder is too big!")
    elif plan == "running around":
        print("We cannot escape that way! The boulder is moving too fast!")
    elif plan == "cross bridge ahead":
        print("That might just work! Lets go!")
    else:
        print("We cannot escape that way! The boulder is in the way!")

def cross_bridge(insteps):
    for i in range(insteps):
        print("Crossed step.")
    if insteps >5:
        print("The bridge is collapsing!")
    else:
        print("We must keep going!")

def climb_ladder(numstepsremaining, numstepscrossed):
    if numstepsremaining > numstepscrossed:
        print("Still some way to go!")
    else:
        print("We are almost there!")

def display_ladder(steps):
    for i in range(steps):
        print("╬═╬")

def create_ladder():
    print("How many steps do you want?")
    steps = int(input())
    display_ladder(steps)


def sum_weights(charweight, invweight):
    total_weight = charweight + invweight
    return total_weight


def calc_avg_weight(charweight, invweight):
    return sum_weights(charweight, invweight) / 2


def run():
    weight = float(input("What is the weight of the character: "))
    inv = float(input("What is the weight of the inventory: "))
    cal = input("What would you like to calculate (sum or average)? ")

    if cal == "sum":
        print (sum_weights(weight, inv))
    elif cal == "average":
        print (calc_avg_weight(weight, inv))
    else:
        print ("Invalid option. Please choose 'sum' or 'average'.")


