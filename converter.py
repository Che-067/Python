# weight converter

weight = float(input("Enter your weight: "))

unit = input("Kilogram or Pound? (Kg or Ib): ")

if unit == "k":
  weight *= 2.205
  unit = "Ibs"
  print(f"Your weight is: {weight} {unit}")

elif unit == "p":
      weight /= 2.205
      unit = "Kgs"
      print(f"Your weight is: {round(weight,2)} {unit}")

else:
     print(f"{unit} is not valid")