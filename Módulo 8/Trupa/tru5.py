def coletar_dados():
    lista_de_pessoas = []
    while True:
        nome = input("Digite o nome da pessoa (ou 'fim' para terminar): ")
        if nome.lower() == 'fim':
            break
        idade = int(input(f"Digite a idade de {nome}: "))
        lista_de_pessoas.append((nome, idade))
    return lista_de_pessoas

lista_de_pessoas = coletar_dados()

menores = tuple(nome for nome, idade in lista_de_pessoas if idade < 18)
maiores = tuple(nome for nome, idade in lista_de_pessoas if idade >= 18)

print("Menores de idade que não poderão entrar:", menores)
print("Maiores de idade que poderão entrar:", maiores)