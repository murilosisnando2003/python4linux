#!/usr/bin/python3
import psycopg2


nome = input("Informe um nome")
idade = input("Informe uma idade")
email = input("Informe um email")

try:
    con = psycopg2.connect('host=localhost dbname=projeto user=admin password=4linux port=5432')
    cur = con.cursor()

    id = con.cursor()   
    id.execute("select max(id) from pessoas")
    id2 = id.fetchall()
    print(id2[0][0])

    cont = id2[0][0]

    cont +=1 

    cur.execute("insert into pessoas (id,nome,email,idade) values ({},'{}','{}','{}') ".format(cont,nome,email,idade))
    # conteudo = cur.comm
    # conteudo = cur.fetchall()
    con.commit()

    cur.execute("select * from pessoas")

    conteudo = cur.fetchall()

    #fetchall fetchone
    print(conteudo)
except Exception as e:
    print('Erro Conection {}'.format(e))