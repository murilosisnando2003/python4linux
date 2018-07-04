#!/usr/bin/python3



def boas_vindas(*args):
    for arg in args:
        print("Ola {}, seja bem vindo!".format(arg))

    print(args)    
    print(len(args))


boas_vindas('daniel', 'rafael','lucia')


