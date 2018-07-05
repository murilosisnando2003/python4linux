#!/usr/bin/python3


class Dog():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.energia = 5
        
    def latir(self):
        print('Au Au!')

    def andar(self):
        self.energia -= 1
        print('andando.... energia: {}'.format(self.energia))   

    def dormir(self):
        self.energia == 10
        print('dormindo.... energia: {}'.format(self.energia))        
     
    def cansado(self):
        if self.energia < 5 :
            print('cansado.... energia: {}'.format(self.energia))    


dog1 = Dog('bilu',2)      
dog2 = Dog('Python',3)
print(dog1.idade)
dog1.latir()
dog1.andar()
dog1.andar()
dog1.andar()
dog1.cansado()
dog1.dormir()