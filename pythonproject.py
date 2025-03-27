print("Biryani")








print("Which kind of biryani do you want to eat?")

biryani = ["1. Chicken", "2. Mutton", "3. beef", "4. Fish", "5. Veg"]
bprice = {"1" : 190, "2" : 260, "3" : 200, "4" : 120, "5" : 100}
print(biryani)

choice = input("Which one do you want to eat? ")
print("Which drink do you want to have with biryani?")
drinks = ["1. Coke", "2. Pepsi", "3. Fanta", "4. Sprite", "5. 7up"]
dprice = {"1" : 50, "2" : 50, "3" : 50, "4" : 50, "5" : 50}
print(drinks)
choiced = input("Which one do you want to drink? ")

order = int(choice)
orderd = int(choiced)

print("You have ordered", biryani[order-1], "biryani")
print("You have ordered", drinks[orderd-1], "drink")

total = bprice[choice] + dprice[choiced]
print("total price", total)


