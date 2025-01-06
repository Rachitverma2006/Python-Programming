  
availableItems = {
    1: {"Items": "Biscuits", "Quantity": 5, "Cost/Item": 20.5},
    2: {"Items": "Chocolates", "Quantity": 10, "Cost/Item": 35},
    3: {"Items": "Coffee", "Quantity": 25, "Cost/Item": 55},
    4: {"Items": "Chips", "Quantity": 10, "Cost/Item": 50},
    5: {"Items": "Cream", "Quantity": 5, "Cost/Item": 30},
}

def display_available_items(arr):
    print("\t\tAvailable Items")
    print(f"{'S.no':<15}{'Item':<15}{'Quantity':<15}{'Cost/Item':<15}")

    for sno, value in arr.items():
        print(
            f"{sno:<15}{value['Items']:<15}{value['Quantity']:<15}{value['Cost/Item']:<15}"
        )

def display_user_cart(dct):
    print("\t\tItems in Cart")
    print(f"{'S.no':<15}{'Item':<15}{'Quantity':<15}{'Total Cost':<15}")

    for sno, value in dct.items():
        print(
            f"{sno:<15}{value['Items']:<15}{value['Quantity']:<15}{value['TotalCost']:<15}"
        )

userDemand = {"Biscuits": 5, "Chocolates": 10, "Coffee": 25, "Chips": 10, "Cream": 5}
name = "Rachit"
address = "Mathura"
distance = 18
deliveryCharge = distance * 2

bill = 0
user_cart = {}

for item in userDemand:
    for i in availableItems:
        if availableItems[i]["Items"].lower() == item.lower():
            if availableItems[i]["Quantity"] >= userDemand[item]:
                amount = userDemand[item] * availableItems[i]["Cost/Item"]
                bill += amount

                availableItems[i]["Quantity"] -= userDemand[item]
                user_cart[i] = {
                    "Items": availableItems[i]["Items"],
                    "Quantity": userDemand[item],
                    "TotalCost": amount,
                }
            else:
                print(f"Sorry, We don't have enough {item} in stock.")
                break

display_user_cart(user_cart)

totalbill = bill + deliveryCharge
customer_details = {"Name":name,"Address":address,"Distance":distance,"Delivery Charge":deliveryCharge,'Bill':bill}
print(f"Total Item Cost {bill}")
print(f"Total Bill Amount {totalbill}")
print(customer_details)
