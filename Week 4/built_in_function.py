print ("Program Started!")
print("Please enter a letter")
letter = input()
if len(letter) == 1:
    ascii = ord(letter)
    print(f"The ASCII code for {letter} is {ascii}")
else:
    print("Error: Please enter a single letter")
print("Program Ended!")

print("Program started!")
code = abs(int(input("Please enter an ASCII code:")))
if code in range(32,127):
    character = chr(code)
    print(f"The character represented by the ASCII code {code} is {character}")
else:
    print("Please enter a value between 32 and 126")
print("Program Ended!")

