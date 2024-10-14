def checa_panagrama(frase):
    letras = set(frase.lower())
    alfabeto = set("abcdefghijklmnopqrstuvwxyz")
    
    if alfabeto.issubset(letras):
        return True
    else:
        return False

frase1 = "The quick brown fox jumps over the lazy dog"
frase2 = "Python é uma linguagem de programação"

print("Entrada:", frase1)
print("Saída:", "É um panagrama" if checa_panagrama(frase1) else "Não é um panagrama")

print("Entrada:", frase2)
print("Saída:", "É um panagrama" if checa_panagrama(frase2) else "Não é um panagrama")
