def meal_price_calculator():
  child_meal = float(input("what is the price of a child's meal ?\n"))
  adult_meal = float(input("what is the price of an adult's meal ?\n"))
  children = int(input("how many children are there ?\n"))
  adults = int(input("how many adults are there ?\n"))
  
  subtotal= (child_meal * children) + (adult_meal * adults)
  
  print(f"The total price is: {subtotal}")

meal_price_calculator()