temperature=float(input("Enter the current temperature: "))
unit=input("Enter unit kelvin or celcius(K or C: )")

if unit == "K":
  temperature = temperature - 273.15
  unit="C"
  print(f"The surrounding temperature is: {temperature} {unit}")
elif unit == "C":
  temperature = temperature + 273.15
  unit="K"
  print(f"The surrounding temperature is: {temperature} {unit}")
else:
  print(f"Invalid {unit}")

