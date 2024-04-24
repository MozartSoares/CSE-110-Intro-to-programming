def meal_price_calculator():
  child_meal = float(input("What is the price of a child's meal ?\n"))
  adult_meal = float(input("What is the price of an adult's meal ?\n"))
  children = int(input("How many children are there ?\n"))
  adults = int(input("How many adults are there ?\n"))
  subtotal= ((child_meal * children) + (adult_meal * adults)) 
  
  print(f"Subtotal: ${subtotal}")
  
  sales_tax_rate = float(input("What is the sales tax rate ?\n")) / 100
  sales_tax = round(sales_tax_rate * subtotal,2)
  total = round(subtotal * (1 + sales_tax_rate),2)

  print(f'Sales tax: ${sales_tax} \nTotal: ${total}')
  
  payment_amount = float(input("What is the payment amount ?\n"))
  change = round(payment_amount - total,2)
  
  print(f"Your change: ${change}")

meal_price_calculator()