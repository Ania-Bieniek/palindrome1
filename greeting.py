# moduł sys ze zmienną argv-która przetrzymuje wszystkie argum. programu.
import sys
def customized_hello(first_name, last_name):
    print("Hello %s %s!" % (first_name, last_name))
if __name__ == "__main__":
    print(sys.argv)
    customized_hello("John", "Clase")
# w terminalu pojawi się powitnie i na początku argumenty-lista-nasz skrypt ma argum.
# kiedy podamy więcej arg. powinny być wyselekcjonowane w naszej zmiennej argv (modyfikujemy print)
    print(sys.argv[1:])
# testujemy skrypt python greetings.py 1 2  
# wpisz całą ścieżkę c:/Users/Mateusz/palindrome_1/venv/greeting.py - potem 1, 2
# lub python .\venv\greeting.py - potem 1 2 

# skrypt musi wpisać imie i nazwisko albo wychodzi. Zabezpieczymy się testując liczbę argum. Jeśeli jest ich za mało to wychodzimy ze skryptu komendą exit. wywołujęmy tu parametrem 1 czyli bład
if len(sys.argv) < 3:
    exit(1)

import sys

def customized_hello(first_name, last_name):
    print("Hello %s %s!" % (first_name, last_name))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        exit(1)
    first_name = sys.argv[1]
    last_name = sys.argv[2]
    customized_hello(first_name, last_name)
    
