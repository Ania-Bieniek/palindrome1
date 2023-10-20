import sys
import logging
logging.basicConfig(level=logging.DEBUG)

      
def calc_1(x, y, choice):
    if choice == 1:
        logging.info(f"Dodaję {x} i {y}")
        print(x + y)

def calc_2(x, y, choice):
    if choice == 2:
        logging.info(f"Odejmuję {y} od {x}")
        print(x - y)

def calc_3(x, y, choice):
    if choice == 3:
        logging.info(f"Mnożę {x} i {y}")
        print(x * y)
           
def calc_4(x, y, choice):
    if choice == 4:
       logging.info(f"Dzielę {x} przez {y}")
       print(x / y) 

calc = calc_1, calc_2, calc_3, calc_4

def start():
    while True:
        choice = int(input("Podaj działanie posługując się odpowiednią liczbą: 1 Dodawanie 2 Odejmowanie 3 Mnożenie 4 Dzielenie:"))
        x = float(input("Wpisz 1 cyfrę:"))
        y = float(input("Wpisz 2 cyfrę"))
        choice = int(choice)
        calc[0](x, y, choice) or calc[1](x, y, choice) or calc[2](x, y, choice) or calc[3](x, y, choice)
        
       
if __name__ == "__main__":
    start()
    calc()














