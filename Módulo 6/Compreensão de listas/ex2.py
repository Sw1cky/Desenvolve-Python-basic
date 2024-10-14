frase= input("Digite uma frase: ")

vogais= "AEIOUaeiou"

lista_de_vogal = sorted([char for char in frase if char in vogais])

lista_de_consoante =[char for char in frase if char.isalpha() and char not in vogais ]

print("Vogal:", lista_de_vogal)
print("Consoante:", lista_de_consoante)