def comprimir_tuplas(lista_trupa):
    acumulador ={}
    for palavra, numero in lista_trupa:
        if palavra in acumulador:
            acumulador[palavra] += numero
        else:
            acumulador[palavra] = numero

    return list(acumulador.items())

tuplas_original = [('maçã', 3), ('banana', 2), ('maçã', 5), ('laranja', 1), ('banana', 3)]
resultado = comprimir_tuplas(tuplas_original)
print(resultado)