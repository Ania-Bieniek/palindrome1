# ćwiczenia dla orłów
# mod 3 zad 4 - gra rzut 1-dną kostką, w każdej kolejce gracz 2 razy rzuca kostką, wynik to suma rzut 1 i 2 
dice = {}
for a in range(1,7):
    for b in range(1,7):
        dice.setdefault(a+b,set())
        dice[a+b].add((a,b))
print(dice[3])

# mod 3 zad 1
numbers = [5, 32, 56, 2, 2, 16, 7, 10, 23, 100]
mean_number = 0
  # 1a zaokrąglij każdy elem. numbers do pełnej 10(5->10, 32->30)
for i,n in enumerate(numbers):
  tens = n//10
  remainder = 10 if n%10 >= 5 else 0
  numbers[i] = tens*10 + remainder
print(numbers)
  # 2a znajdź i pozbądź się największego i najmniejszego ele. zmodyf. listy
numbers.remove(min(numbers))
numbers.remove(max(numbers))
print(numbers)
  # 3a policz średnią z ostat. zmodyf. listy numbers i przypisz do zmiennej mean_number
mean_number = sum(numbers) / len(numbers)
print(mean_number)

# zad 2 Budujemy most

# zbuduj funkcję  która będzie True jeżeli mając płytę o dł. zmiennej chunk np 4 to zbudujemy most o dł zmiennej goal np 40
# mając jeszcze do budowy łącznik = połowa chunk
# False gdy przy użyciu podanych wartości zminnych chunk i goal nie można zbudowąć mostu
def build_bridge(chunk, goal):
   junction = chunk / 2
   x = (goal + (junction * 1)) / (chunk + junction)
   return True if x.is_integer() else False
print(build_bridge(4, 40))











    
    





     




    




          
          






    





    

    





    


    





