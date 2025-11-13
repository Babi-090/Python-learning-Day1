#weightConverter
weight=float(input("Enter your weight: "))
unit=(input("Enter the unit kilogram or gram(K or G): "))

if unit == "K":
  weight=weight*1000
  unit="gram"
  print(f"The weight is {weight} {unit}")
elif unit == "L":
  weight=weight/1000
  unit="kg"
  print(f"The weight is {weight} {unit}")
else:
  print(f"The {unit} is invalid")


