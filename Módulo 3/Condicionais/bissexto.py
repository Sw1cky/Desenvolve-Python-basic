ano = int(input("digite o ano: "))

def bissexto_ano(ano):
 if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    return "bissexto"

 else: 
      return "não bissexto"
 

resultado = bissexto_ano(ano)
print(f"Ano {ano}: {resultado}")
