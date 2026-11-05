from validtion import *
from orders import *
from function import *


         

def choice():
  while True:
    menu()
    choose = input("Choose option:")
    if choose == "1":
        Shopping_Cart(products)       
    elif choose == "2":
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