#!/usr/bin/python3

#ler o nome de dois alunos
aluno = input("Informe o nome do aluno: ")
aluno = aluno.lower()
aluno = aluno.replace('a','@')
aluno = aluno.strip()

# ler duas notas e calcular a media
nota1 = float(input("Informe a primeira nota:"))

nota2 = float(input("Informe a segunda nota:"))

resultado = ((nota1 + nota2) / 2)

if resultado >= 7:
    result = 'aprovado'
elif resultado < 7 and resultado > 4:
    result = 'recuperação'
else:
    result = 'reprovado'

#mostrar a media e a nota do aluno
print(aluno, "Nota média do aluno: ", resultado)

print  ("O aluno  {} tem a media {} e esta {}".format(aluno, resultado,result))