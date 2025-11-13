principle=0
rate=0
time=0
while True:
  principle=float(input("Enter the principle amount:  "))
  if principle <0:
    print("Principle cannot be negative")
  else:
   break
while True:
  rate=float(input("Enter rate:  "))
  if rate <0:
    print("rate cannot be negative")
  else:
   break
while True:
  time=float(input("Enter the time in years:  "))
  if time <0:
    print("time cannot be negative")
  else:
    break



amount=principle*pow((1+rate/100),time)
CI=amount-principle
print(f"Total amount after {time} years: {amount:.2f}")
print(f"Compound Interest: {CI:.2f}")