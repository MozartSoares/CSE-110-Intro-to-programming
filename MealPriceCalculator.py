#In addition to the requirements, I've added the payment amount validation and the option to add a tip to the total amount

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
  
  wants_tip = input("Do you want to add a tip to support the waiter?, (please answer with y/n) \n")
  if wants_tip == "y":
    recommended_amount = round(total * 0.1,2)
    print(f"The recommended tip amount is ${recommended_amount}, but feel free to include any other value you wish")
    tip_amount = float(input("What is the tip amount ?\n"))
    total = round(total + tip_amount,2)
    print(f"Thanks for supporting the waiter, your new total with the tip is ${total}")

  while True:
        payment_amount = float(input("What is the payment amount ?\n"))
        if payment_amount < total:
            print("Insufficient funds. Please try again.")
        else:
            break

  change = round(payment_amount - total,2)
  
  print(f"Your change is: ${change}")
  print(f"Thanks for using our meal price calculator !")

meal_price_calculator()

while True:
  pass