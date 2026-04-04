name = input("Enter the User name: ")
mobile_number = input("Enter the Mobile Number: ")
mem_ship = input("Are you a Premium Member: ")
restau_deta = input("Is restaurant opened or Not: ")
order_amount = int(input("Enter the Order Amount: "))
if restau_deta == "opened":
    print("The Restaraunt is open")

    if mem_ship == "yes | opened | open":
        
        if order_amount >= 1500:
            print(f"You have gained 15% discount {discount = order_amount * 0.85} your Total amount {order_amount - discount}")
        elif order_amount >= 1000:
            print(f"You have gained 10% discount {discount = order_amount * 0.90} your Total amount {order_amount - discount}")
        elif order_amount >= 700:
            print(f"You have gained 5% discount {discount = order_amount * 0.05} your Total amount {order_amount - discount}")
    
    else:
        print("You are not a Premium Member")
        
else:
    print("Restaurant is Closed")
