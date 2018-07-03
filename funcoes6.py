#!/usr/bin/python3

numero = int(input('informe um numero: '))

def valida_num(numero):
    if numero % 2 == 0:
        return 'Par'
    else:
        return 'Impar'


a = valida_num(numero)
print(a)