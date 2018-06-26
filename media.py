#!/usr/bin/python3

#ler o nome de dois alunos
aluno = input("Informe o nome do aluno: ")
aluno = aluno.lower()
aluno = aluno.replace('a','@')
aluno = aluno.strip()

# ler duas notas e calcular a media
nota1 = int(input("Informe a primeira nota:"))

nota2 = int(input("Informe a segunda nota:"))

resultado = ((nota1 + nota2) / 2)

#mostrar a media e a nota do aluno
print(aluno, "Nota média do aluno: ", resultado)

print  ("O aluno  {} tem a media {}".format(aluno, resultado))