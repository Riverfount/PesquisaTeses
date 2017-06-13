import sqlite3


with sqlite3.connect("tesesDissertacoes.db") as conexao:
    for registro in conexao.execute("""select id, instituicao, programa, autor_trabalho, 
                                              titulo_trabalho, data_defesa, link 
                                      from tesesDissertacoes 
                                      order by id"""):

        print('{0[0]}'.format(registro))
        # print('{0[1]}'.format(registro))
        # print('{0[2]}'.format(registro))
        # print('{0[3]}'.format(registro))
        print('{0[4]}'.format(registro), '\n')
        # print('{0[5]}'.format(registro))
        # print('{0[6]}'.format(registro))

