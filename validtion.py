from orders import *


def chek_id_products(num):
    id = int(num)
    for p in products:
        if p["id"] == id:
            return True
    print("Product id not found")
    return False

def chek_num(num):
    try:
     id = int(num)
     if id <= 0:
        print("Positive numbers only")
        return False
     return True
    except ValueError:
        print("Numbers Only!") 
        return False
    

def chek_id_orders(num):
    id = int(num)
    for order in orders:
        if order["id"] == id:
            return True
    print("order id not found")
    return False

def Discount_Calculation(price):
    if price < 300:
        return price
    elif price < 700:
        return price * 0.95
    elif price < 1500:
        return price * 0.9
    else:
        return price * 0.85