from validtion import *
def menu():
  print("========== ORDER MANAGER ==========")
  print("1. Create order")
  print("2. Show all orders")
  print("3. Find order by ID")
  print("4. Close order")
  print("5. Show sales report")
  print("0. Exit")
 
  


def create_order1():
     id = input("Enter the product ID")
     if chek_num(id) and chek_id_products(id) == True :
          quantity = input("Enter desired quantity")
          if chek_num(quantity) == True:
               create_order0(id,quantity)


def create_order0(id,quantity):
    cart = []
    total = 0
    order=    {
          "id": 0,
          "items": 0,
          "total": 0,
          "status": "OPEN"
              }
    for p in products:
         if p["id"] == id:
              total += p["price"] * quantity
    order["id"] = len(orders) + 1
    order["items"] = [{"product_id": id, "quantity": quantity}]


def Shopping_Cart(products):
       total = 0
       cart = []   
       more = True   
       while more == True:
        id = input("Enter the product ID:")
        if chek_num(id) and chek_id_products(id) == True :
          quantity = input("Enter desired quantity:")
          if chek_num(quantity) == True:
            create_order0(id,quantity)
            cart.append(  {"product_id": id, "quantity": quantity})
            for product in products:
              if product["id"] == to_int(id):
                total += product["price"] * to_int(quantity)
            print("Would you like to add more products?")
            more = input("for yes enter 1")
            if more == "1":
                 more = True
            else:
                 more = False                      
        order=    {
                  "id": 0,
                  "items": 0,
                  "total": 0,
                  "status": "OPEN"
                      }
       order["id"] = len(orders) + 1
       order["items"] = cart
       order["total"] = Discount_Calculation(total)
       orders.append(order)
       print("The order was placed successfully.")
       print(f"Shopping Cart:{cart}")
       print("The price before the discount:",total)  
       print("The price after the discount",Discount_Calculation(total))  

       
            


def all_orders(): #2
     for order in orders:
          print(order)




def find_order():   #3
      id = input("Enter the order ID")  
      if chek_num(id) and chek_id_orders(id) == True:
           for order in orders:
                if order["id"] == int(id):
                     print(order)
         
         
























