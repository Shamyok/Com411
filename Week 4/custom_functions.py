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
escape_by("jumping over")
escape_by("running around")
escape_by("cross bridge ahead")