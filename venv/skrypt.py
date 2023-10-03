#kiedy wiemy jakie argumenty od użytk. będą nam potrzebne, możemy podać je od razu przy uruchomieniu( argumenty skryptu)
# gdybyśmy tą  funkcję zamkili w pliku stworzylibyśmy skrypt
def custimized_hello(first_name, last_name):
    print("Hello %s %s!" % (first_name, last_name))
#wpisujemy dane "na sztywno"
if __name__ == "__main__":
    custimized_hello("John", "Clase")

# moduł sys ze zmienną argv-która przetrzymuje wszystkie argum. programu.
import sys
def customized_hello(first_name, last_name):
    print("Hello %s %s!" % (first_name, last_name))
if __name__ == "__main__":
    print(sys.argv)
    customized_hello("John", "Clase")


    