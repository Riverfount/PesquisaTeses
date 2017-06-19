import sqlite3


with sqlite3.connect("tesesDissertacoes.db") as conexao:
    print(f'{"GRAU ACADÊMICO":<25} QUANTIDADE')
    total = 0
    for registro in conexao.execute("""SELECT grau_academico, count(grau_academico) 
                                          FROM tesesDissertacoes
                                          GROUP BY grau_academico"""):
        total += int(registro[1])

        print(f'{registro[0].upper():<25} {registro[1]:10d}')

    print(f'\n{"Total".upper():<25} {total:10d}')
