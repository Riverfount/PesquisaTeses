import sqlite3


with sqlite3.connect("tesesDissertacoes.db") as conexao:
    print('programa; quantidade')
    for registro in conexao.execute("""SELECT programa, count(programa) 
                                          FROM tesesDissertacoes
                                          GROUP BY programa"""):

        print('{0[0]}; {0[1]}'.format(registro))
