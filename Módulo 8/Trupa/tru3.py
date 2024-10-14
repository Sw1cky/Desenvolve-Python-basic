def ordenar_tuplas(lista_de_tuplas):
    return sorted(lista_de_tuplas, key=lambda aluno: aluno[1], reverse=True)

alunos_notas = [('Alice', 8.5), ('Bob', 7.2), ('Charlie', 9.0), ('David', 8.8)]
resultado = ordenar_tuplas(alunos_notas)
print(resultado)