print ("escolha entre as classes: mago, guerreiro e arqueiro")
input("escolho a classe: ")
ponto_força = int(input(("Digite os pontos de força: ")))
ponto_magia = int(input(("Digite os pontos de magia: ")))

guerreiro = ponto_força >= 15 and ponto_magia <= 10
mago = ponto_força <=10 and ponto_magia >= 15
arqueiro = ponto_força >= 5 and ponto_magia >= 5 and ponto_força <= 15 and ponto_magia < 15

print (guerreiro)
print (mago)
print (arqueiro)