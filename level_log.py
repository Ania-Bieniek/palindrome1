
# poziomy logowania/ zamist print wywołujemy logging
# do logów możemy dołączyć czas zdażenia i nazwa loggera
import sys
import logging
                                    # dodajemy znacznik czasowy zdażeń   # konfiguracja, żeby logi trafiały do pliku               
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile.log")
# wyświetli w konsoli date i godzine
def print_maturity(age):
    if age >= 18:
        logging.info("You are an adult")
    else:
        logging.info("You are a kiddo!")
    
if __name__ == "__main__":
    logging.debug("The program was called with this parametres %s" % sys.argv[1:])
    logging.debug("First parametr is %s" % sys.argv[1])
    age = int(sys.argv[1])
    print_maturity(age)
    
   # wywołanie w konsoli ...palindrome> python level_log.py 33 Zosia

# logowanie danych do pliku jest wygodne, bo informacje o tym gdzie i kiedy 
# został uruchomiony nasz program sa zapisywne na dysk
# żeby skonfigurować wystarczy - argument logfile do funkcji basicConfig 
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile.log")
# OD TEGO MOMENTU LOGI TRAFIAJĄ DO PLIKU logfile.log (na pasku zadań po lewej stronie w plikach!!)

# boblioteka loging umożliwia pełną kontrolę nad tym, co i gdzie trafia (bez błędów) podczas logowania.
# dlatego porzuć print gdy zaczynasz pisać dla klientów!!!




    
