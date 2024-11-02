mountains = int(input("How many mountains should I display?"))
print("Displaying...")
for loop in range(mountains):
    print ("""\        _    .  ,   .           .
    *  / \_ *  / \_      _  *        *   /\'__        *
      /    \  /    \,   ((        .    _/  /  \  *'.
 .   /\/\  /\/ :' __ \_  `          _^/  ^/    `--.
    /    \/  \  _/  \-'\      *    /.' ^_   \_   .'\  *
  /\  .-   `. \/     \ /==~=-=~=-=-;.  _/ \ -. `_/   \
 /  `-.__ ^   / .-'.--\ =-=~_=-=~=^/  _ `--./ .-'  `-
/        `.  / /       `.~-^=-=~=^=.-'      '-._ `._""")
print("Done!")

steps = int(input("How far are we from the target?"))
for loop in range(steps):
    print(f"{steps} steps remaining")
    steps -= 1

i = 0
brightness = int(input("What level of brightness is required?"))
print("Adjusting brightness...")
for loop in range(2,brightness+1, 2):
    print(f"Brightness level: {'*'*loop}")


word = input("What word do you see?")
x = len(word)
i = 0
print("Displaying index positions...")
for loop in range(x):
    print (word[i])
    i += 1
