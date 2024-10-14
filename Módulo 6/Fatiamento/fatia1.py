
fatia = [int(input("Digite um número inteiro: ")) for _ in range(4)]
while True:
    pergunta= input("QUER adicionar mais um número? (s/n): ").strip().lower()
    if pergunta == 's':
        fatia.append(int(input("Digite um número inteiro: ")))
    elif pergunta == 'n':
        break
    else:
        print("Resposta da pergunta inválida. use 's' ou 'n'.")

print(f"\nLista original: {fatia}")
print(f"Os 3 primeiros elementos: {fatia[:3]}")
print(f"Os 2 últimos elementos: {fatia[-2:]}")
print(f"Lista invertida: {fatia[::-1]}")
print(f"Elementos de índice par: {fatia[::2]}")
print(f"Elementos de índice ímpar: {fatia[1::2]}")