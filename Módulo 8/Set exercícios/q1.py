def caracteres_unicos(string):
    caracteres = set(string.lower())
    caracteres_ordenados = sorted(caracteres)
    return caracteres_ordenados

frase = "O rato roeu a roupa do Robson"

caracteres_unicos_ordenados = caracteres_unicos(frase)

print("Caracteres únicos ordenados:", caracteres_unicos_ordenados)
