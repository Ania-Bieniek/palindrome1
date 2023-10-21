
import sys
import logging
logging.basicConfig(level=logging.DEBUG)

      
def add(x, y):
    return(x + y)

def sub(x, y):
    return(x - y)

def multiply(x, y):
    return(x * y)
           
def divide(x, y):
    return(x / y) 

calc = add, sub, multiply, divide

def start():
    while True:
        choice = int(input("Podaj działanie posługując się odpowiednią liczbą: 1 Dodawanie 2 Odejmowanie 3 Mnożenie 4 Dzielenie:"))
        x = float(input("Wpisz 1 cyfrę:"))
        y = float(input("Wpisz 2 cyfrę"))
        choice = int(choice)
        if choice == 1:
          calc[0](x, y) 
        elif choice == 2:
            calc[1](x, y)
        elif choice == 3:
            calc[2](x, y)
        elif choice == 4:
            calc[3](x, y)
        result = calc(x,y)
        print(result) # nie rozumiem dlaczego nie działa... 
       
if __name__ == "__main__":
    start()
    calc()