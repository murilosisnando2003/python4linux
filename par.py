#!/usr/bin/python3

'''
ler numero e verificar se ele é par ou impar e adicionar ele em uma lista com o resultado

[2, 'par']
[3,'impar']

'''
lista = [1,2,3]
numero = int(input('informe um numero: '))
print (numero % 2 )

# nomes.append(['branco','pardo'])

if numero % 2 == 0:
    lista.append(numero)
    print('este numero é par')
else:
    print('este numero é impar')

print(lista)
