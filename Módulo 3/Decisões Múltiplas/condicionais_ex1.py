
def calculadora():
    try:
        operando_primeiro = float(input("Digite o primeiro número: "))
        operador = input("Digite o operador (+, -, *, /, **): ")
        operando_segundo = float(input("Digite o segundo número: "))
        
        if operador == '+':
            resultado = operando_primeiro + operando_segundo
        elif operador == '-':
            resultado = operando_primeiro - operando_segundo
        elif operador == '*':
            resultado = operando_primeiro * operando_segundo
        elif operador == '/':
            if operando_segundo != 0:
                resultado = operando_primeiro / operando_segundo
            else:
                return "Errado: Divisão por zero não é permitida."
        elif operador == '**':
            resultado = operando_primeiro ** operando_segundo
        else:
            return "Errado: Operador inválido."
        
        return f"Resultado: {resultado}"
    
    except ValueError:
        return "Errado: Entrada inválida. coloque numeros corretos."

print(calculadora())