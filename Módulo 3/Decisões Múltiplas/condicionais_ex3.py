def Avalia_desempenho(pontuacao):
    if pontuacao >= 90:
        return "Excelente"
    elif pontuacao >= 80:
        return "Bom"
    elif pontuacao >= 70:
        return "Regular"
    else:
        return "Insatisfatório"

try:
    pontuacao = float(input("Digite a pontuação do jogador: "))
    classificacao = Avalia_desempenho(pontuacao)
   
    print(f"Classificação: {classificacao}")
except ValueError:
    print("Errado: coloque um valor valido")