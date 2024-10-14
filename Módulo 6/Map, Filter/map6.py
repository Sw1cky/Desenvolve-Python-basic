
import random
lista = [random.randint(1, 100) for _ in range(20)]

def dividir_lista(lista, tamanho):
    return [lista[i:i+tamanho] for i in range(0, len(lista), tamanho)]

while True:
    print("Listagem original:")
    print(lista)
    
    tamanho_divisao = int(input("Tamanho para divisão: "))
    if tamanho_divisao == 0:
        break
    
    sublistas = dividir_lista(lista, tamanho_divisao)
    print("Subslistas:")
    print(sublistas)