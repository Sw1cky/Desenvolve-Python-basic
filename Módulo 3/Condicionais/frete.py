dist = float(input("Digite a distância de entrega em quilometros: "))
peso = float(input("Digite o peso da encomenda em quilogramas: "))
def calcula_frete(dist, peso):
      
 if dist  >= 100:
     taxa_por_kg  = 1.0
 elif 101 <= dist <= 300:
     taxa_por_kg  = 1.50
 else:
     taxa_por_kg  = 2.0
 if peso > 10:
  valor_frete += 10.0
  valor_frete = taxa_por_kg   *  peso
  valor_frete = calcula_frete(dist, peso)
 print(f"O valor do frete é: R${valor_frete:.2f}")
