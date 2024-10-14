import random

escolha_numero = random.randint(1, 10)

while True: 

    escolha = int(inpur("Tente adiinhar o numero de 1 a 10: "))

    if escolha > escolha_numero:
         print("Muito alto< tente de novo")

    elif escolha < escolha_numero:
         print("Muito baixo, tente de novo")
    
    else:
        print("Resposta corrrte, o numero secreto é", escolha_numero)
        break

    escolha_numero()
