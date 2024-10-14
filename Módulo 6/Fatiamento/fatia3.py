import random
import itertools


lista = [random.randint(-10, 10) for _ in range(20)]

print("Original: ", lista)

maior_intervalo_inicio = 0
maior_intervalo = 0
inicio = 0
atual = 0

for i, num in enumerate(lista):
    if num < 0:
        atual += 1
    if  atual > maior_intervalo:
        maior_intervalo_inicio = inicio
        maior_intervalo = atual
else:
    inicio = i + 1
    atual = 0

del lista[maior_intervalo_inicio:maior_intervalo_inicio + maior_intervalo]
print("Edição sem maior intervalo negativo:", lista) 