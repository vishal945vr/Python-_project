# CAFE Management system
# menu list
Menu={
    "Pizza":150,
    'Pasta':50,
    'Burger':60,
    "salad":30,
    "Coffee":80,
    "Cake":30,


}
print("welcome to ROCK STARE Restaurant")
# print menu
print("Pizza:150\nPasta:50\nBurger:60\nsalad:30\nCoffee:80")
# add item  for memu
item_1=input("Enter the name of item you want to order: ")
# this code  for add the amount for item
order_total=0
if(item_1 in Menu):
    order_total+=Menu[item_1]
    print(f"Your item {item_1} has been added to your order ")
 
   
else:
    print(f"Ordered item {item_1} is not avaialable yet!")

    # this code for added the another item in menu
    
another_item=input("you want to another item(Yes/No):")
if another_item=="Yes":
    item_2=input("Eneter your order:")
    if item_2 in Menu:
        order_total+=Menu[item_2]
        print(f"Item{item_2} has been added to order")
else:
    print(f"Order item is {item_1}not avaiable")
    # show amount to pay 
print(f"The Total Amount of item to Pay:{order_total}")

   







