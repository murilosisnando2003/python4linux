#!/usr/bin/python3

class  Car():
    def __init__(self, ano, modelo,marca):
        self.ano = ano
        self.modelo = modelo
        self.marca = marca

    def acelerar(self):
        print('acelerando....')

    def freiar(self):
        print('freiando....')        
