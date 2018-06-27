#!/usr/bin/python3

# numeros = list(range(40,100))
# nomes = ['daniel','joao','maria']


# for nome in nomes:
#     print(nome.title())


# nomes2 = []

# for nome in nomes:
#     nomes2.append(nome)


# print(nomes2)


num = int(input("informe um numero: "))

for x in range(num):
    if x % 2 == 0:
        print("{} par".format(x))

    else:
        print("{} impar".format(x))