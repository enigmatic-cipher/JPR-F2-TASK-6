"""
Modify the class ShoppingItem in Task3. Create a suitable constructor. Add a method printItem in the class. Create two objects of ShoppingItem. Print their details and also the total bill amount.
"""

class shoppingItems:
  def __init__(self, item_code, description, price, discount):
    self.item_code = item_code
    self.description = description
    self.price = price
    self.discount = discount

  def __str__(self):
    return "Shopping Detail: Item Code: {}, Description: {}, Price: {}, & Discount: {}".format(self.item_code,self.description,self.price,self.discount)

total_price = 0
total_discount = 0

n = int(input("Enter number of items: "))

for i in range(0,n):
  item_code = int(input("Enter item code: "))
  item_description = input("Enter Description: ")
  item_price = int(input("Enter Price: "))
  total_price = total_price + item_price
  discount_on_item = int(input("Enter Discount: "))
  total_discount = total_discount + discount_on_item
  lst = shoppingItems(item_code, item_description, item_price, discount_on_item)
  print("*******************\n")
  print(f"{lst}\n")
  print("*******************\n")

bill = (total_discount/100) * total_price

print(f"Plaese pay total bill amount: {total_price - bill} $\n")
print("Thank You For Shopping With Us\n")
print("Good Day :)")