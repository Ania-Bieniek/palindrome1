#przykład użycia argumentów, przebieg programu zależny od płci pracownika
print("Witaj, ten program pomoże Ci sprawdzić cz jesteś pełnolietni/a")
adult = None
sex = input('K')
if sex == 'M':
  age = int(input("Twój wiek?"))
  agult = age >= 18
elif sex == 'K':
  print("Kobiet o wiek się nie pyta, więc zrobię to delikatnie.")
  over18_yesno = input('T')
  adult = (over18_yesno == 'T')
else: 
  print("Nie ma takiej płci!")
  exit(1)
print("Już wiem. Twoja pełnoleniość w boolean to %s" % str(adult))













