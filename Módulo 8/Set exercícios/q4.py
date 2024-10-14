
def encontra_elemento_diferente(lista1, lista2):
    diferenca = set(lista1) - set(lista2)
    if diferenca:
        elemento_diferente = diferenca.pop()
        lista_desfalcada = "segunda" if elemento_diferente in lista1 else "primeira"
        print(f"O elemento {elemento_diferente} está faltando na {lista_desfalcada} lista")
    else:
        print("As listas são idênticas")

lista1 = [1, 4, 5, 7, 9]
lista2 = [4, 5, 7, 9]

encontra_elemento_diferente(lista1, lista2)

