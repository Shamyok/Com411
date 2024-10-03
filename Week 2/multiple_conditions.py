adventure = input("What type of adventure should I have?")
if adventure == "scary" or adventure == "short":
    print("Entering the dark forest!")
elif adventure == "safe" or adventure == "long":
    print("Taking the safe route!")
else:
    print("Not sure which route to take")

noise = input("What did I hear?")
sight = input("What did I see")
if noise =="grr" and sight =="two red eyes":
    print("There is a scary creature. I should get out of her!")
else:
    print("I am a little scared but I will continue.")
