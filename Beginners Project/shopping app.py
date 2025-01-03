availableItems = {1:{'Items':'Biscuits','Quantity':5,'Cost/Item':20.5},
                  2:{'Items':'Chocolates','Quantity':10,'Cost/Item':35},
                  3:{'Items':'Coffee','Quantity':25,'Cost/Item':55},
                  4:{'Items':'Chips','Quantity':10,'Cost/Item':50},
                  5:{'Items':'Cream','Quantity':5,'Cost/Item':30}
                  }


def display_available_items(arr):
    
    print("\t\tAvailable Items")
    print(f"{"S.no":<15}{"Item":<15}{"Quantity":<15}{"Cost/Item":<15}")
    
    for sno , value in arr.items():
        print(f"{sno:<15}{value["Items"]:<15}{value["Quantity"]:<15}{value["Cost/Item"]:<15}")

display_available_items(availableItems)
    