
new_name = "Jasio"
with open("new_names_txt", 'w') as write_file:
    write_file.write(new_name)
print(new_name) # po print nowe okno do wyświetlania zawartości new_name.txt


new_name = "Czesio"
with open("new_names.txt", 'a') as write_file:
    write_file.write(new_name)
print(new_name)
  

new_name = "Stasio"
with open("new_names.txt", 'a') as write_file:
    write_file.write(new_name)
print(new_name)

new_name = "Misio"
with open("new_names.txt", 'a') as write_file:
    write_file.write(new_name)
print(new_name)

new_name = "Zdzisio"
with open("new_names.txt", 'a') as write_file:
    write_file.write(new_name)
print(new_name)

with open("new_names.txt", 'r') as read_file:
    for line in read_file.read().splitlines():
        print(line)
        
        









