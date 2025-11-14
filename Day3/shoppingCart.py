cart=[]

while True:
  food=input("Enter food you want to buy and q to quit: ")
  if food == "q":
    break
  else:
    price=float(input(f"Enter the price of {food}:Rs. "))
    cart.append([food,price]) 
print("---Your Cart---")
total=0
for item in cart:
  print(f"{item[0]} - Rs.{item[1]}")
  total=total+item[1]
print(f"Your total is:Rs.{total}")