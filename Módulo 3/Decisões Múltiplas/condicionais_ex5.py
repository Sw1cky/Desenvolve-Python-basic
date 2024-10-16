## Não altere os atributos definidos a seguir
iris1_a1, iris1_a2, iris1_a3 = 123, 456, 789
iris2_a1, iris2_a2, iris2_a3 = 987, 654, 321
iris3_a1, iris3_a2, iris3_a3 = 111, 222, 333
iris4_a1, iris4_a2, iris4_a3 = 444, 555, 666



tolerancia = 5

def autenticar(a1, a2, a3):
    if (abs(a1 - iris1_a1) <= tolerancia and 
        abs(a2 - iris1_a2) <= tolerancia and 
        abs(a3 - iris1_a3) <= tolerancia):
        return "Autenticação ocorreu sem problemas! Usuário: 1"
    
    elif (abs(a1 - iris2_a1) <= tolerancia and 
          abs(a2 - iris2_a2) <= tolerancia and 
          abs(a3 - iris2_a3) <= tolerancia):
        return "Autenticação ocorreu sem problemas! Usuário: 2"
    
    elif (abs(a1 - iris3_a1) <= tolerancia and 
          abs(a2 - iris3_a2) <= tolerancia and 
          abs(a3 - iris3_a3) <= tolerancia):
        return "Autenticação ocorreu sem problemas! Usuário: 3"
    
    elif (abs(a1 - iris4_a1) <= tolerancia and 
          abs(a2 - iris4_a2) <= tolerancia and 
          abs(a3 - iris4_a3) <= tolerancia):
        return "Autenticação ocorreu em problemas! Usuário: 4"
    
    else:
        return "Autenticação falhou!"


print("Insira o padrão de íris para autenticação.")
a1 = int(input("Atributo 1: "))
a2 = int(input("Atributo 2: "))
a3 = int(input("Atributo 3: "))

resultado = autenticar(a1, a2, a3)
print(resultado)