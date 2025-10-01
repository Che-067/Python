

unit = input("Is this temperature in celsius,Kelvin or Fahrenheit (C,K,F): ")
temp = float(input("enter the temperature: "))

if unit == "c":
  kelvin = temp + 273 
  fahrenheit = (temp * 9/5) + 32
  print(f"Your results are: {str(kelvin) + " K"}, {str(fahrenheit) + " F"}")
elif unit == "k":
      celcius = temp - 273
      fahrenheit = (temp -273) * 9/5 + 32
      print(f"Your results are: {str(celcius) + " C"}, {str(fahrenheit) + " F"}")
elif unit == "f":
      kelvin = (temp -32) * 5/9 + 273
      celcius = (temp -32) * 5/9
      print(f"Your results are: {str(kelvin) + " K"}, {str(celcius) + " C"}")
else:
    print(f"{unit}  is invalid")




