import sqlite3


with sqlite3.connect("tesesDissertacoes.db") as conexao:
    print('instituicao; quantidade')
    for registro in conexao.execute("""SELECT instituicao, count(instituicao) 
                                          FROM tesesDissertacoes
                                          GROUP BY programa"""):

        print('{0[0]}; {0[1]}'.format(registro))
