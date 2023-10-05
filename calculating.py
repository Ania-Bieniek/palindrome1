
import sys
import logging

logging.basicConfig(level=logging.DEBUG)

def calculating(x, y, choice):
    if choice == 1:
        logging.info(f"Dodaję {x} i {y}")
        print(x + y)
    elif choice == 2:
        logging.info(f"Odejmuję {y} od {x}")
        print(x - y)
    elif choice == 3:
        logging.info(f"Mnożę" {x} "i" {y})
        print(x * y)
    elif choice == 4:
        logging.info(f"Dzielę" {x} przez {y}")
        print(x / y) 
    else:
        print("Zły wynik")


if __name__ == "__main__":
    choice = int(input("Podaj działanie posługując się odpowiednią liczbą: 1 Dodawanie 2 Odejmowanie 3 Mnożenie 4 Dzielenie:")) 
    x = int(input("Podaj pierwszą liczbę:"))
    y = int(input("Podaj drugą liczbę:"))
    calculating("wynik" x, y, choice)










    




