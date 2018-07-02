#!/usr/bin/python3


def leitura(x):
  try:  
    with open (x,'r+') as arquivo:
            var = arquivo.readlines()
    return var        
  except Exception as e:
    print("Arquivo Ineixstente: {}".format(x))              
    


a = leitura('frutas222.txt')
print(a)