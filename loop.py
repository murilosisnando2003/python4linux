#!/usr/bin/python3

# cont = 0

# while cont >=10:
#     print('executo')
#     cont += 1

nomes = []


while True:
    nome = (input("Digite um nome ou sair para sair "))

    if nome.lower().strip() == 'sair':
        break 
    nomes.append(nome)
    print('nome: {}'.format(nomes))
