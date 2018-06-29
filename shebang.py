#!/usr/bin/python3

nome = input("Digite o nome do arquivo: ")

with open(arquivo, 'r+') as arquivo:
    arquivo.seek(0)
    arquivo.write('#!/usr/bin/python3\n')
