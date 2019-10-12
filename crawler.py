import math
from contextlib import closing
import requests
import json
import sqlite3

URL = 'http://catalogodeteses.capes.gov.br/catalogo-teses/rest/busca'
HEADERS = {'Content-type': 'application/json', 'Accept': 'text/plain'}

anos = [{"campo": "Ano", "valor": year} for year in range(2009, 2019)]

DATA = {'termo': '"Epistemologia Genética" "Psicologia Genética" Piaget', 'registrosPorPágina': 20, 'filtros': anos}


def fetch_page(page_number):
    payload = DATA.copy()
    payload['pagina'] = page_number

    while True:
        response = requests.post(URL, headers=HEADERS, data=json.dumps(payload))

        if 200 <= response.status_code < 300:
            return response.json()
        else:
            continue


def get_total_pages(response):
    total = response['total']
    per_page = response['registrosPorPagina']
    return math.ceil(total / per_page)


if __name__ == '__main__':

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
