#!/usr/bin/python3

def boas_vindas(**kwargs):
    # for arg in kwargs:
        print("Ola {} {}, sejam bem vindo!".format(kwargs['nome'],kwargs['sobrenome']))


boas_vindas(nome='Daniel',sobrenome='Rodrigues')


