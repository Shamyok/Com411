apples = 0
apples = int(input("How many apples should I remove?"))

for i in range(apples):
  print("Removed apple")

obstacles = 0
obstacles = int(input("How many obstacles should I avoid?"))
while obstacles >0:
  print(f"Avoiding...Done!{obstacles} obstacles avoided.")
  obstacles -= 1
print("All obstacles have been avoided")