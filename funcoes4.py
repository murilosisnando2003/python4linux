#!/usr/bin/python3


def escrever_arq(nome_arq, conteudo):
    try:
        with open(nome_arq,'w') as arq:
            for x in conteudo:
                arq.write(x + '\n')
            return True
    except Exception as e:
        return 'Erro: {}'.format(e)        

nomes = ['daniel', 'pedro', 'joao', 'julio']
escrever_arq('nomes.txt', nomes)       