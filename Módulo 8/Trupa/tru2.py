def encontrar_vogais(frase):
    vogais = 'aeiouAEIOU'
    for indice, letra in enumerate(frase):
        if letra in vogais:
            print(f"Vogal: {letra}, Índice: {indice}")

frase = "O rato roeu a roupa da Alice"
encontrar_vogais(frase)
