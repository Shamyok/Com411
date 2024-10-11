rows = int(input("How many rows should I have?"))
columns = int(input("How many columns should I have?"))
print("Here I go:")
for i in range(rows):
    for j in range(columns):
        print(":-)", end=" ")
    print()