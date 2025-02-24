import random
lista=[]
antal_6=0
for tal in range(10):
    tal=random.randint(1,6)
    lista.append(tal) 
    if tal == 6:
        antal_6=antal_6+1
lista.sort(reverse=True)
print(lista)
print('summa', sum(lista))
medelvarde= sum(lista)/len(lista)
print('medelvärde:', medelvarde)
print('minsta tal:', min(lista))
print('största tal:', max(lista))
print('Antal sexor:', antal_6)

