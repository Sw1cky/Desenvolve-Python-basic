 #Entrada de dados
 #genero, idade itempode serviço
genero = input("Digite seu genero, m ou f: ") 
idade  = int(input("Digite sua idade: "))
tempo  = int(input("Digite seu tempo de serviço: "))

#processamento
a = ((genero == 'f' and idade >= 60) or int(genero == 'm' and idade >= 65)) 
b = tempo >= 30
c = idade >= 60 and tempo >= 25

#saida
if(a or b or c):
    print("Pode aposentar")
else:
    print("Não pode aposentar")


