primeiro_num = float(input("digite o primeiro numero:"))
segundo_num = float(input("Digite o segundo número: "))

diferença_absoluta = abs(primeiro_num - segundo_num)

arredondamento = round(diferença_absoluta, 2)

print(f"Adiferença absoluta entre os numeros é: {diferença_absoluta}")