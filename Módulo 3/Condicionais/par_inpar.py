#entrada dos numeros
n1, n2 = int(input("De o primeiro numero: ")), int(input("De o segundo numero: "))

#Processamento
if ((n1 + n2) % 2) == 0:
     
#saida de daos
     print("É par!")
else:
     print("È inpar!")

print("par!" if (n1 + n2) % 2 == 0 else "impar!")