#!/usr/bin/python3

def valor_total(**kwargs):
    # for arg in kwargs:
        return kwargs['preco'] * kwargs['qtd']
        

a = valor_total(preco=2, qtd=10)
print(a)


