import sqlite3


with sqlite3.connect("tesesDissertacoes.db") as conexao:
    print('programa; quantidade')
    for registro in conexao.execute("""SELECT programa, count(programa) 
                                          FROM tesesDissertacoes
                                          GROUP BY programa"""):

        print(f'{registro[0]}; {registro[1]}')
