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
