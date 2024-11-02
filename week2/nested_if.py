cover = input("What type of cover does the book have?")
if cover == "soft":
   question = input("Is the book perfect-bound?")
   if question == "yes":
       print("Soft cover, perfect bound books are very popular!")
elif cover == "hard":
    print("Books with hard covers can be more expensive!")
else:
    print("Soft covers with coils or stiches are great for short books")

response = input("Where should I look")
if response == "in the bedroom":
    bedroom = input("Where in the bedroom should I look?")
    if bedroom == "under the bed":
      print("Found some shoes but no phone")
    else:
        print("Found some mess but no phone")
elif response == "in the bathroom":
  bathroom = input("Where in the bathroom should I look?")
  if bathroom == "in the bathtub":
      print("Found a rubber duck but no phone")
  else:
      print("Found bathroom stuff but no phone")
elif response == "in the living room":
    living_room = input("Where in the living room should I look?")
    if living_room == "on the table":
        print("Yes! I found my phone!")
    else:
        print("Found some stuff but not my phone")
else:
    print("I do not know where that is but I will keep looking")

