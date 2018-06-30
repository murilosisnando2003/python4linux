#!/usr/bin/python3


try:
    num = int(input("Digite um numero: "))
    print(num)
except ValueError as e:
    print("Não é um inteiro: {}".format(e))
except Exception as e:
    print("Erro genérico: {}".format(e))


