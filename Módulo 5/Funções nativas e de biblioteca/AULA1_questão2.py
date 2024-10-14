#entrada de dado
import random
import math

#calculo
n = int(input("digite o valor de n: "))

valor= [random.randint(0, 100) for _ in range(n)]

calculo = sum(valor)

raiz = math.sqrt(calculo)

#saida de dados
print(f"Asoma dos numeros é: {calculo}")
print(f"A raiz quadrada da soma dos numeros é: {raiz}")