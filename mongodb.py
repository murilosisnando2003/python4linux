#!/usr/bin/python3

from pymongo import MongoClient

try:
    client = MongoClient()
    db = client['4linux']
except Exception as e:
    print("Erro:{}".format(e))

db.frutas.insert({'_id':1,'nome':'laranja'}, {'_id':2,'nome':'pera'})

# db.pessoas.remove()

# db.pessoas.update({'_id':5}, {'$set' : {'sobrenome': 'silva'}})


# dados = db.pessoas.find()
# dados = [x for x in dados]
# print(dados)