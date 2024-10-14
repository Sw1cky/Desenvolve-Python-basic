import math

lista_de_raio= [1.5, 0.8, 2.3, 5.0]
calculo_da_area = lambda r: round(math.pi * (r ** 2), 2)
areas = list(map(calculo_da_area, lista_de_raio))

print(areas)