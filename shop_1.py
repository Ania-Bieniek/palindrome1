#skrypt który pobiera pojedyńczy tekst-rozdzielony przecinkami- a następnie tworzy opis naszych zakupów
def shopping(items, payment='card', shop='lokal shop'):
    result = ""
    result = result + "Idę na zakupy do %s.\n" % shop
    result = result + "Kupuję następujące rzeczy: \n"
    for item in items:
        result = result + " - %s\n" % item
    result = result + "By zapłacić, używam %s." % payment
    return result

if __name__ == "__main__":
   items_text = input("Podaj produkty rozdzielone przecinkiem:")
   items = items_text.split(',')
shopping_result = shopping(items)
print(shopping_result) 



    





















