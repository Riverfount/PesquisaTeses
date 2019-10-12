import sqlite3


def consulta(campos, order='', group=''):
    querystring = 'select ' + campos + ' from tesesDissertacoes'
    if order != '':
        querystring += ' order by ' + order

    if group != '':
        querystring += ' group by ' + group

    with sqlite3.connect("tesesDissertacoes.db") as conexao:
        for registro in conexao.execute(querystring):
            print('{} --- {}'.format(registro[0], registro[1]))


if __name__ == "__main__":
    consulta(campos='id, instituicao', group='instituicao')

"""
with sqlite3.connect("tesesDissertacoes.db") as conexao:
     for registro in  conexao.execute('SELECT id, instituicao, programa FROM tesesDissertacoes ORDER BY id'):
         print('{0[0]:<2}; {0[1]:<70}; {0[2]:<30}'.format(registro))
"""
