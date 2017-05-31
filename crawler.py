import math
from contextlib import closing
import requests
import json
import sqlite3

URL = 'http://bancodeteses.capes.gov.br/banco-teses/rest/busca'
HEADERS = {'Content-type': 'application/json', 'Accept': 'text/plain'}

ano = [{"campo": "Ano", "valor": "2008"}, {"campo": "Ano", "valor": "2009"}, {"campo": "Ano", "valor": "2010"},
       {"campo": "Ano", "valor": "2011"}, {"campo": "Ano", "valor": "2012"}, {"campo": "Ano", "valor": "2013"},
       {"campo": "Ano", "valor": "2014"}, {"campo": "Ano", "valor": "2015"}, {"campo": "Ano", "valor": "2016"}]

DATA = {'termo': '"Epistemologia Genética" "Psicologia Genética" Piaget', 'registrosPorPágina': 20}


def fetch_page(page_number):
    payload = DATA.copy()
    payload['pagina'] = page_number

    while True:
        response = requests.post(URL, headers = HEADERS, data = json.dumps(payload))

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
        response = fetch_page(1)

        if current == 1:
            total = get_total_pages(response)

        for dissertation in response['tesesDissertacoes']:
            print(dissertation)
            output.append(dissertation)

        current += 1  # let's go to the next page (the while condition blocks a non-existent page)


    '''
    dados = []
    for saida in output:
        dados.append((saida['id'], saida['instituicao'], saida['nomePrograma'], saida['municipioPrograma'],
                      saida['titulo'], saida['autor'], saida['dataDefesa'], saida['volumes'], saida['paginas'],
                      saida['biblioteca'], saida['grauAcademico'], saida['link']))

    with sqlite3.connect("tesesDissertacoes.db") as conexao:
        with closing(conexao.cursor()) as cursor:

            cursor.execute(""" CREATE TABLE tesesDissertacoes(id integer primary key autoincrement, codigo text, 
            instituicao text, programa text, municipio text, titulo_trabalho text, autor_trabalho text, 
            data_defesa text, num_volumes text, num_paginas text, biblioteca text, grau_academico text, link text)""")

            cursor.executemany(""" INSERT INTO tesesDissertacoes(codigo, instituicao, programa, municipio, 
            titulo_trabalho, autor_trabalho, data_defesa, num_volumes, num_paginas, biblioteca, grau_academico, 
            link) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?); """, dados)

            conexao.commit()

            print("Base de dados criada e populada com sucesso!")

    '''