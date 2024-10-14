def diferente_lists(lista1, lista2):
    return list(set(lista1) - set(lista2))

list1 = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
list2 = [1, 1, 2, 4, 5, 6]
resultado = diferente_lists(lista1, lista2)

print("Diferença entre as listas:")
print(resultado)