cover = input("What type of cover does the book have?")
if cover == "soft":
   question = input("Is the book perfect-bound?")
   if question == "yes":
       print("Soft cover, perfect bound books are very popular!")
elif cover == "hard":
    print("Books with hard covers can be more expensive!")
else:
    print("Soft covers with coils or stiches are great for short books")

