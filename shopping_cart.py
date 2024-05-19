#I've also added the quantity of the item as an extra information to store and display.

def add_number(operation: str,items:list=[],new_item:str='',  ):
      if operation == 'quantity':
        while True:
          new_value = input("And how much of it would you like to add ? \n")

          try:
            new_value = int(new_value)
            if new_value <= 0:
              print("Invalid quantity please answer with a valid one.")
              continue
            return new_value

          except ValueError:
            print("Invalid quantity please answer with a valid one.")
            continue
          
      if operation == 'price':
        while True:
          new_value = input(f"What is the price of {new_item} ? \n")
          new_value = new_value.replace(",",".")
            
          try:
            new_value = float(new_value)
            if new_value <= 0:
              print("Invalid price please answer with a valid one.")
              continue
            return new_value

          except ValueError:
            print("Invalid price please answer with a valid one.")
      
      while True:
        new_value = input(f"Which item would you like to remove ?\n")

        try:
          new_value = int(new_value)
          if new_value <= 0 or new_value > len(items):
            print("Sorry, that is not a valid item number.")
            continue
          return new_value - 1
        except ValueError:
          print("Sorry, that is not a valid item number.")

def add_item(items,prices):
  new_item = input("What item would you like to add ? \n")
  new_item_price = add_number(new_item=new_item,operation="price")
  new_quantity = add_number(new_item=new_item,operation="quantity")

  items.append({new_item: new_quantity})
  prices.append({new_item: new_item_price})
  
  new_item_price = f"$ {new_item_price:.2f}"
  print(f"{new_quantity} '{new_item}' has been added to cart at the price of {new_item_price}")
  return items,prices

def remove_item(items,prices): 
    view_cart(items,prices)
    item_to_be_removed_index = add_number(operation='remove',items=items)
    item_to_be_removed = items[item_to_be_removed_index]
    
    for nome_item, preco_item in item_to_be_removed.items():
      confirmation = input(f"Are you sure you want to delete {nome_item} with price $ {preco_item} ? (answer with y/n)\n")
  
    if confirmation == 'y':
      for nome_item, preco_item in item_to_be_removed.items():
        print(f"{nome_item} was removed from the cart")
      del items[item_to_be_removed_index]
      del prices[item_to_be_removed_index]
      return items,prices
    return items,prices

def view_cart(items,prices):
  if len(items) == 0:
    print("The shopping cart is empty.")
    return
  
  print("The contents of the shopping cart are:\n")
  
  for i, item in enumerate(items, start=1):
    for item_name, quantity in item.items():
      price = prices[i-1][item_name] 
      print(f"{i}. {item_name} - Quantity: {quantity}, Price: $ {price:.2f}")
  print('\n')

def calculate_total(items,prices):
  total_price = 0
  
  for i, item in enumerate(items, start=1):
    for item_name, quantity in item.items():
      price = prices[i-1][item_name] 
      summed_up_price = price * quantity
      total_price += summed_up_price
      
  print(f"The total price of the items in the shopping cart is $ {total_price:.2f}")

def exit():
  print("Thanks for using the shopping cart program, goodbye !.")

def main():
  items = []
  prices = []
  
  print("Welcome to the shopping cart !")
  
  while True:
    print("""Please select one of the following: 
        1. Add item
        2. View cart
        3. Remove item
        4. Compute total
        5. Quit""")
  
    option = input("please enter an action: ")
  
    if option == '1':
      items,prices = add_item(items,prices)
    elif option == '2':
      view_cart(items,prices)
    elif option == '3':
      items,prices = remove_item(items,prices)
    elif option == '4':
      calculate_total(items,prices)
    elif option == '5':
      exit()
      break
    else:
      print("Invalid option.")

main()

