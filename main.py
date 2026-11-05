from validtion import *

def menu():
  print("========== ORDER MANAGER ==========")
  print("1. Create order")
  print("2. Show all orders")
  print("3. Find order by ID")
  print("4. Close order")
  print("5. Show sales report")
  print("0. Exit")
 
  


products = [
            {"id": 1, "name": "Keyboard", "price": 120},
            {"id": 2, "name": "Mouse", "price": 80},
            {"id": 3, "name": "Monitor", "price": 900},
            {"id": 4, "name": "Headphones", "price": 200},
            {"id": 5, "name": "USB Cable","price": 30}
           ]
orders = [{
          "id": 1,
          "items": [{"product_id": 1, "quantity": 2},
                     {"product_id": 3, "quantity": 1}],
          "total": 1026.0,
          "status": "OPEN"
          },{
          "id": 2,
          "items": [{"product_id": 1, "quantity": 2},
                     {"product_id": 3, "quantity": 1}],
          "total": 1026.0,
          "status": "closs"
          }]
order =   {
          "id": 1,
          "items": [{"product_id": 1, "quantity": 2},
                     {"product_id": 3, "quantity": 1}],
          "total": 1026.0,
          "status": "OPEN"
          }





def create_order1():
     id = input("Enter the product ID")
     if chek_num(id) and chek_id_products(id) == True :
          quantity = input("Enter desired quantity")
          if chek_num(quantity) == True:
               create_order0(id,quantity)

def create_order0(id,quantity):
    order=    {
          "id": 0,
          "items": [],
          "total": 0,
          "status": "OPEN"
              }
    for p in products:
         if p["id"] == id:
              order["total"] = p["price"] * quantity
    order["id"] = len(orders) + 1
    order["items"] = [{"product_id": id, "quantity": quantity}]
    orders.append(order)
    print("The order was placed successfully.")


def all_orders(): #2
     for order in orders:
          print(order)




def find_order():   #3
      id = input("Enter the order ID")  
      if chek_num(id) and chek_id_orders(id) == True:
           for order in orders:
                if order["id"] == int(id):
                     print(order)
         
         

























def choice():
  while True:
    menu()
    choose = input("Choose option:")
    if choose == "1":
        create_order1()       
    elif choose == "2":
         create_order0()
         all_orders()
    elif choose == "3":
            find_order()
    elif choose == "4":
            print("4")             
    elif choose == "5":
            print("5") 
    elif choose == "0":
            exit()
    else:
         print("Enter a number between 1 and 5 only; to exit, press 0.")                        

choice()         