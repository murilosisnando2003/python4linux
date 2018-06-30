#!/usr/bin/python3

from datetime import datetime

users = ['daniel','pedrooo','maria','joao']
try:
    while True:
        num = input('''
        USER
        0 - daniel
        1 - pedro
        2 - maria
        3 - joao
        S - sair ''')
        if num.lower() == 's':
            break
        print (users[int(num)])
except IndexError as e:
    d = datetime.now()
    with open('erro.txt','a') as arquivo:    
        arquivo.write("{} - {}\n".format(d.strftime("%Y-%m-%d %H:%M"),e)    
    print("Usuário inexistente")