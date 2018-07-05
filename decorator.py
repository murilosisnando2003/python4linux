#!/usr/bin/python3

def meu_decorator(linguagem)
    def func():
        print('A linguagem é: %s' %linguagem)
        return linguagem()
    return func

@meu_decorator
def linguagem():
    return('Python')

linguagem()

