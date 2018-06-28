#!/usr/bin/python3

# with open('frutas.txt','a') as arquivo:
#     print(arquivo.read("Limao\n")



#!/usr/bin/python3
# with open('frutas.txt','r') as arquivo:
#     print(arquivo.readline())
#     print(arquivo.readline())
#     arquivo.seek(0)
#     print(arquivo.readline())

while True:
    fruta = input('Digite uma fruta: ') 
    if fruta.strip().lower()=='sair':
        break
    with open('frutas.txt','a') as arquivo:    
        arquivo.write("{}\n".format(fruta))    
    