import sqlite3


with sqlite3.connect("tesesDissertacoes.db") as conexao:
    print('id; instituição; programa; autor; título; data defesa; link')
    for registro in conexao.execute("""SELECT id,
                                              instituicao,
                                              programa,
                                              autor_trabalho,
                                              titulo_trabalho,
                                              data_defesa,
                                              link
                                          FROM tesesDissertacoes
                                          GROUP BY id"""):

        print('{0[0]}; {0[1]}; {0[2]}; {0[3]}; {0[4]}; {0[5]}; {0[6]}'.format(registro))
