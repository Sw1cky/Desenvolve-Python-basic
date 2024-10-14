#Entrada de dados
comprimento = int(input("Digite ocomprimento: "))
largura     = int(input("Digite a largura: "))
preco_m2    = float(input("valor do m2: "))
#proçesamento de dados
area = comprimento * largura #m2
preço_total = area * preco_m2

print(f"O terreno possui {area}m2 e custa R${preço_total:,.2f}")
