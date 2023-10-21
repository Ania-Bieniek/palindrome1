
import sys
import logging

logging.basicConfig(level=logging.DEBUG)

def calc(x, y, choice):
    if choice == 1:
        print(x + y)
    elif choice == 2:
        print(x - y)
    elif choice == 3:
        print(x * y)
    elif choice == 4:
        print(x / y) 
   

while True:
  if __name__ == "__main__":
    choice = int(input("Podaj działanie posługując się odpowiednią liczbą: 1 Dodawanie 2 Odejmowanie 3 Mnożenie 4 Dzielenie:")) 
    if int(choice) > 5:
        exit(1)
    x = float((input("Podaj pierwszą liczbę:")))
    y = float((input("Podaj drugą liczbę:")))
    choice = int(choice)
    calc(x, y, choice)
    
     
    





2




    






    
























    




