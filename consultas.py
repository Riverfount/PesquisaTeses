import sqlite3


def consulta(campos, order='', group = ''):

    lista_final = ''
    querystring = 'select ' + campos + ' from tesesDissertacoes'
    if order != '':
        querystring += ' order by ' + order

    if group != '':
        querystring += ' group by ' + group

    with sqlite3.connect("tesesDissertacoes.db") as conexao:
        for registro in conexao.execute(querystring):
            lista_intermediaria = ''
            for r in registro:
                lista_intermediaria += r.lower() + '|'
            lista_final += lista_intermediaria
    return lista_final


if __name__ == "__main__":

    dados = consulta(campos = 'programa', group = 'programa')

    for char in dados:
        if char == '|':
            print(';')
            continue
        else:
            print(char, end = '')
