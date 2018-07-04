#!/usr/bin/python3

import pdb

def manipular_arquivo(nome, modo='r', conteudo=None):

    if modo == 'r':
        with open(nome,modo) as arquivo: 
            return arquivo.readlines() 
    elif modo == 'a':
        with open(nome,modo) as arquivo:
            conteudo = arquivo.readlines()
            arquivo.write(conteudo+'\n')
                         
# pdb.set_trace()

while True:
    arq = input('Digita o nome do arquivo ou sair: ')
    if arq == 'sair':
        break
    print(manipular_arquivo(arq))