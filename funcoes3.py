#!/usr/bin/python3

def escrita(nome,conteudo):

 try:
    with open(nome,'a') as arquivo:    
        arquivo.write("{}\n".format(conteudo))
    return 'True'       
 except Exception as e:
    print("Arquivo Inexistente: {}".format(nome))        


a = escrita('frutas.txt','Acerola')
print(a)