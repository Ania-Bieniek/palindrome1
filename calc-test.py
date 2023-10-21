import sys
import logging
logging.basicConfig(level=logging.DEBUG)

      
def add(x, y):
    return (x + y)

def sub(x, y):
    return (x - y)

def multiply(x, y):
    return (x * y)
           
def divide(x, y):
    return (x / y) 

operations = {
    "1":add,
    "2":sub,
    "3":multiply,
    "4":divide
}

def start():
    while True:
        choice = input("Podaj działanie posługując się odpowiednią liczbą: 1 Dodawanie 2 Odejmowanie 3 Mnożenie 4 Dzielenie:")
        if int(choice) > 4:
          exit(1)
        x = float(input("Wpisz 1 cyfrę:"))
        y = float(input("Wpisz 2 cyfrę:"))
        result = operations[(choice)](x,y)
        print(result)
        

if __name__ == "__main__":
    start()
    operations()
    















