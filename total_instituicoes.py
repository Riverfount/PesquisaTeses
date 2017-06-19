import sqlite3


with sqlite3.connect("tesesDissertacoes.db") as conexao:
    print('instituicao; quantidade')
    for registro in conexao.execute("""SELECT instituicao, count(instituicao) 
                                          FROM tesesDissertacoes
                                          GROUP BY programa"""):

        print(f'{registro[0]}; {registro[1]}')
