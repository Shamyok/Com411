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

i = 1
bar = int(input("How many bars should be charged?"))
while i <=bar:
  print(f"Charging:{'█'*i}")
  i +=1
print("The battery is fully charged")

phrase = (input("Please type a phrase"))
x = len(phrase)
print("hi "*x)

print("Calculating the sum of the first 100 numbers...")
num = 100
sum = 0
for i in range(num+1):
  sum += i
print(f"...Done! The answer is {sum}.")

tally = 0
i=1
num = int(input("How many numbers should I sum up?"))
while i <= num:
    answer = int(input(f"Please enter number {i} of {num}"))
    tally += answer
    i +=1
print(tally)





