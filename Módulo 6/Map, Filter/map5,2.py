def pares_unicos(numeros, soma_objetivo):
    numeros_set = set(numeros)

    pares = []
    for num in numeros_set:
        complemento = soma_objetivo - num
        if complemento in numeros_set and complemento != num:
           pares.append((min(num, complemento), max(num, complemento)))
    return pares

# Exemplo de uso: 
nums = [3, 4, 5, 6, 7]
soma = 10
resultado = pares_unicos(nums, soma)
print(resultado)  # Saída esperada: [(3, 7), (4, 6)]