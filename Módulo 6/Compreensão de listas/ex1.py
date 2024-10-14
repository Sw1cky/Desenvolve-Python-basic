pares_no_raio = [num for num in range (20, 50) if num % 2 == 0]

quadrado = [num ** 2 for num in [1, 2, 3, 4, 5, 6, 7, 8 ,9]]

dividido = [num for num in range(1, 101) if num % 7 == 0]

par_ou_impar = ["par"if num % 2 == 0 else "impar" for num in range(0, 30, 3)]

print("Pares no raio de 20 e 50:", pares_no_raio)
print("Os quadrados dos valores da lista [1,2,3,4,5,6,7,8,9]:", quadrado)
print("Todos os números entre 1 e 100 divisíveis por 7:", dividido)
print("'Par' ou 'Impar' para valores no raio de (0,30,3):", par_ou_impar)