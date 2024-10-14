n =int(input("digite o valor de 'n' prara a matriz: "))

def produza_matriz(n):
    matriz = [[x * y for y in range(n)] for x in range(n)]
    return matriz

matriz = produza_matriz(n)

print("matriz: ")
for linha in matriz:
    print(linha)
