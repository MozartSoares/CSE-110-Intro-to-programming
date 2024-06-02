#Windchill (F) = 35.74 +0.6215t - 35.75(v**0.16)+0.4275T(v**0.16)
#I didn't include any additional creativity because it is not required for full grade in this assignment. 
def calculate_windchill(t,unit):
  v = 5
  if unit == "C":
    t = celsius_to_fahrenheit(t)
  while v <= 60:
    windchill = 35.74 + 0.6215*t - 35.75*(v**0.16) + 0.4275*t*(v**0.16)
    print(f"At temperature {t:.1f}F, and wind speed {v} mph, the windchill is: {windchill:.2f}F")
    v += 5

def main():
  while True:
    try:
      t = float(input("What is the temperature ? \n"))
      break
    except ValueError:
      print("Please insert a valid number.")
  while True:
    unit = input("Fahrenheit or Celsius (F/C)? \n").upper()
    if unit in ["F", "C"]:
      break
    else:
      print("Please insert a valid answer (F/C).")
  calculate_windchill(t, unit)

def celsius_to_fahrenheit(t):
    return t * 9/5 + 32


main()