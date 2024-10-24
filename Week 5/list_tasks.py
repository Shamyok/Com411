def directions():
    print(list(["Move forward", "Move backward", "Turn left", "Turn right"]))

directions()

path = ["Move forward", 10, "Move backward", 5 , "Move Left", 3 , "Move Right", 1]
print("Moving...")
for i in range(0, len(path), 2):
    print(f"{path[i]} for {path[i+1]}")