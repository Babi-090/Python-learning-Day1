#shopping cart program
foods=[]
prices=[]
total=0
while True:
  food=input("Enter food you want to buy and q to quit: ")
  if food == "q":
    break
  else:
    price=float(input(f"Enter price of a {food}:Rs"))
    foods.append(food)
    prices.append(price)
print("-----YOUR CART-----")
for food in foods:
  print(food, end="\n")
for price in prices:
  total=total+price
print(f"Your total amount is:Rs.{total}")