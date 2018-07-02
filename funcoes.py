#!/usr/bin/python3

def somar(x, y):
    return x + y

b = somar(3,2)
print(b)

exit()

def boas_vindas(nome,idade=24):
    return('Ola sou o {} e tenho {} anos '.format(nome,idade))


a = (boas_vindas('maria',25)  )  
# print(boas_vindas('jose',30))

print(a)

