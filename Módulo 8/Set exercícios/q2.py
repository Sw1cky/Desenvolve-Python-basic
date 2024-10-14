def tem_elementos_comuns(lista1, lista2):
    set1 = set(lista1)
    set2 = set(lista2)
    return bool(set1.intersection(set2))

lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6, 7]
resultado = tem_elementos_comuns(lista1, lista2)
print(resultado) 