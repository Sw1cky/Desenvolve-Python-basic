#Leitura de dados 
valor_total = int(input("Digite o valor total: "))


#processamento de dados
####começar da maior nota
notas_100   = (valor_total // 100)
####Atualizar quanto falta da maior nota
#mudar variavel valor_total
valor_total = valor_total % 100
##### segunda maior nota
notas_50    = (valor_total // 50)
valor_total = valor_total % 50
notas_20    = (valor_total // 20)
valor_total = valor_total % 20
notas_10    = (valor_total // 10)
valor_total = valor_total % 10
notas_5     = (valor_total // 5)
valor_total = valor_total % 5
notas_2     = (valor_total // 2)
valor_total = valor_total % 2
notas_1     = (valor_total // 1)
valor_total = valor_total % 1
#Saida de dados 
menor_numero = print(f"O menor valor de notas è {notas_100} de 100, {notas_50} de 50, {notas_20} de 20, {notas_10} de 10, {notas_5} de 5, {notas_2} de 2 é {notas_1} de 1")
print(f"{notas_100} (nota/s) de 100")
print(f"{notas_50} (nota/s) de 50")
print(f"{notas_20} (nota/s) de 20")
print(f"{notas_10} (nota/s) de 10")
print(f"{notas_5} (nota/s) de 5")
print(f"{notas_2} (nota/s) de 2")
print(f"{notas_1} (nota/s) de 1")