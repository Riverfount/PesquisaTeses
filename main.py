import sqlite3
from contextlib import closing
from crawler import fetch_page, get_total_pages

total = 1
current = 1
output = []
while current <= total:
    response = fetch_page(current)

    if current == 1:
        total = get_total_pages(response)

    for dissertation in response['tesesDissertacoes']:
        print(dissertation)
        output.append(dissertation)

    current += 1  # let's go to the next page (the while condition blocks a non-existent page)

dados = []
for saida in output:
    if saida not in dados:
        dados.append((saida['id'], saida['instituicao'], saida['nomePrograma'], saida['municipioPrograma'],
                      saida['titulo'], saida['autor'], saida['dataDefesa'], saida['volumes'], saida['paginas'],
                      saida['biblioteca'], saida['grauAcademico'], saida['link']))

with sqlite3.connect("tesesDissertacoes.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute(""" CREATE TABLE IF NOT EXISTS 
                           tesesDissertacoes(id integer primary key autoincrement, codigo text,
                           instituicao text, programa text, municipio text, titulo_trabalho text, autor_trabalho text,
                           data_defesa text, num_volumes text, num_paginas text, biblioteca text, grau_academico text, 
                           link text)""")

        cursor.executemany(""" INSERT INTO tesesDissertacoes(codigo, instituicao, programa, municipio, 
           titulo_trabalho, autor_trabalho, data_defesa, num_volumes, num_paginas, biblioteca, grau_academico, 
           link) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?); """, dados)

        conexao.commit()

        print("Base de dados criada e populada com sucesso!")
