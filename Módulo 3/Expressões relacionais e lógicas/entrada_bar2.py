#entrada de dados
#idade de Juliana
#idade do cris 
idade_juliana = int(input(f"digite a idade de Juliana: "))
idade_cris = int(input(f"digite a idade do Cris: "))

# processamento de dados
# true se ambos forem maiores de idade
#<exp1> juliana é maior de idade
#<exp2> cris é maios de idade
#false se em qualquer outro caso
pode_entrar = idade_juliana >= 18 or idade_cris >= 18
#saida de dados
print(pode_entrar)