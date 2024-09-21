menu={'Pizza':40, 'Pasta':40,'Coffe':80,'Burger':60,'Salad':70}

print("WELCOMR TO MY INFINTY KITHCHEN")
print("Pizza:Rs40 \nPasta:Rs40 \nCoffe:Rs80 \nBurger:Rs60 \nSalad:Rs70")

Order_total = 0

Item_1 = input("Enter the name of item you want to order = ")
if Item_1 in menu:
    Order_total += menu[Item_1]
    print(f"Your item {Item_1} has been added to your order")
else:
    print(f"ordered item {Item_1} is not avaliable at the moment")

Another_order=input("Do you want to add something else in your order? (Yes/No)")
if Another_order == "Yes":
    Item_2= input("Enter the name of second item = ")
    if Item_2 in menu:
        Order_total += menu[Item_2]
        print(f"Item {Item_2} has been added to order")
    else:
        print(f"ordered item {Item_2} is not avaliable at the movment")

Another_order=input("Do you want to add something else in your order? (Yes/No)")
if Another_order == "No":
    print(f"The total amount of items to pay is {Order_total}")

    print(F"Thankyou for ordering in INFINTY KITCHEN!!")
    print(F"Your order will be ready in 20 Minutes")

