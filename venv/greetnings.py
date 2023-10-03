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


