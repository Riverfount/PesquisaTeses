import requests
import json
import sqlite3
from contextlib import closing

dados = []

cabecalho = {'Content-type': 'application/json', 'Accept': 'text/plain'}
payload = {'termo': "\"Epistemologia Genética\" or \"Psicologia Genética\" or Piaget", 'filtros': [],
           'pagina': 1, 'registrosPorPagina': 40}

r = requests.post('http://bancodeteses.capes.gov.br/banco-teses/rest/busca',
                  headers = cabecalho, data = json.dumps(payload))

dicionario = json.loads(r.text)

for i in range(len(dicionario['tesesDissertacoes'])):
    dados.append([dicionario['tesesDissertacoes'][i]['id'],
                  dicionario['tesesDissertacoes'][i]['municipioPrograma'],
                  dicionario['tesesDissertacoes'][i]['instituicao'],
                  dicionario['tesesDissertacoes'][i]['nomePrograma'],
                  dicionario['tesesDissertacoes'][i]['dataDefesa'],
                  dicionario['tesesDissertacoes'][i]['titulo'],
                  dicionario['tesesDissertacoes'][i]['autor'],
                  dicionario['tesesDissertacoes'][i]['biblioteca'],
                  dicionario['tesesDissertacoes'][i]['paginas'],
                  dicionario['tesesDissertacoes'][i]['grauAcademico'],
                  dicionario['tesesDissertacoes'][i]['volumes'],
                  dicionario["tesesDissertacoes"][i]["link"]])


with sqlite3.connect("tesesDissertacoes.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute("""
                         create table tesesDissertacoes(
                             id integer primary key autoincrement,
                             codigo text,
                             municipio text,
                             instituicao text,
                             programa text,
                             data_defesa text,
                             titulo_trabalho text,
                             autor_trabalho text,
                             biblioteca text,
                             num_paginas text,
                             grau_academico text,
                             num_volumes text,
                             link text)
                         """)
        cursor.executemany("""
                insert into tesesDissertacoes(
                    codigo,
                    municipio,
                    instituicao,
                    programa,
                    data_defesa,
                    titulo_trabalho,
                    autor_trabalho,
                    biblioteca,
                    num_paginas,
                    grau_academico,
                    num_volumes, link)
                    values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                           dados)
        conexao.commit()
        print("Base de dados criada com sucesso!")
