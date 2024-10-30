def listen():
    sound = input("What sound did you hear?")
    print(f"That was a loud {sound}!")

listen()

def identify():
    reponse = input("What lies before us?")
    if reponse.lower() == "a large boulder":
        print("Its time to run!")
    else:
        print("We will be fine.")
identify()
