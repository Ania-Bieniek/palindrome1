# kiedy chcemy uniknąć błędów wywołania programu, możemy zapisać jakie dane się do nich dostają . Spr. z jakimi arg został uruchomiony i zalogujmy całą listę parametrów 
# logowanie do standardowego wyjścia, zalecany sposób logowania z terminala dla mikroserwisów. Z czasem bedzie trzeba zapisywać do pilku i czytanie będzie się wiązać z kontrolą plików
import sys

print("The program was called with this parameters %s" % sys.argv[1:])
# w ten sposób dowiemy sie co ktoś wpisał na start ... wpisz na dole w konsoli python venv/print.py 33

# następnie ważny jest typ parametru-jeżeli ktoś wpisze tekst ktorego nie da sie konwetować na liczbę - nie działa.

print ("The first parametr is %s" % sys.argv[1]) # wpisz w konsoli!!!! python venv/print.py mniam
# a jeżeli wpisze 3 mniam, to w  1 print jest lista ['3' , 'mniam'] a w drugim print tylko 3 




