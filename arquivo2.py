#!/usr/bin/python3
try:
with open ('frutas500.txt','r') as arquivo:
    var = arquivo.readlines()
alterado = []
cont = 1
for linha in var:
    alterado.append('{}-{}'.format(cont, linha))
    cont += 1
    with open('frutas2.txt','a') as arquivo:    
        arquivo.write("{}-{}\n".format(cont,linha))    
print(alterado)        