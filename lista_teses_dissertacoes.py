import sqlite3

with sqlite3.connect("tesesDissertacoes.db") as conexao:
    print('id; instituição; programa; grau_academico; título; data defesa; link')
    for registro in conexao.execute("""SELECT id,
                                              instituicao,
                                              programa,
                                              grau_academico,
                                              titulo_trabalho,
                                              data_defesa,
                                              link
                                          FROM tesesDissertacoes
                                          GROUP BY id"""):
        print(
            f'{registro[0]}; {registro[1]}; {registro[2]}; {registro[3]}; {registro[4]}; {registro[5]}; {registro[6]}'
        )
