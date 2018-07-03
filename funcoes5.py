#!/usr/bin/python3


def alterar_lista(lista):
    lista1 = []
    for x in lista:
        lista1.append('{}\n'.format(x))
    return lista1    


nomes = ['daniel','maria','jose','pedro']

a =alterar_lista(nomes)
print(a)
