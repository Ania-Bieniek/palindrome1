
# w termonalu tworze nowy plik ...palindrome_1> mkdir names.txt cd names.txt git init names.txt

# żeby zapisać coś do pliku trzeba go otworzyć innym trybem, 2 opcje:

# 1 opcja : jeżeli chcemy zapisać całkowicie nowy tekst, wystarczy zmienić tryb na write
new_name = "Milenka"
with open("names_txt", 'w') as write_file:
    write_file.write(new_name)
print(new_name)


# 2 opcja : jeżeli chcemy dopisywać to wtedy append ozn. jako a:
new_name = "Lusia"
with open("names.txt", 'a') as write_file:
    write_file.write(new_name)
print(new_name)

new_name = "Pusia"
with open("names.txt", 'a') as write_file:
    write_file.write(new_name)
print(new_name)

new_name = "Malusia"
with open("names.txt", 'a') as write_file:
    write_file.write(new_name)
print(new_name)

new_name = "Tyciusia"
with open("names.txt", 'a') as write_file:
    write_file.write(new_name)
print(new_name)

# jak odczytać plik txt - dzięki wbudowanej funkcji open, otworzymy go w trybie do odczytu(ang.read) z trybem o symb. r
# skrypt umożliwiający wypisanie linijek  pliku
with open("names.txt", 'r') as read_file:
    for line in read_file.read().splitlines():
        print(line)


