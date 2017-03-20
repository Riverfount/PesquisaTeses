import requests
import json
import sqlite3
from contextlib import closing
import time

def insere_dados(x):
    dados = []
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    payload = {'termo': "\"Epistemologia Genética\" or \"Psicologia Genética\" or Piaget", 'filtros': [],
               'pagina': x, 'registrosPorPagina': 20}

    r = requests.post('http://bancodeteses.capes.gov.br/banco-teses/rest/busca',
                      headers=headers, data=json.dumps(payload))
    dicionario = json.loads(r.text)
    for i in range(len(dicionario['tesesDissertacoes'])):
        dados.append([dicionario['tesesDissertacoes'][i]['id'], dicionario['tesesDissertacoes'][i]['municipioPrograma'],
                     dicionario['tesesDissertacoes'][i]['instituicao'], dicionario['tesesDissertacoes'][i]['nomePrograma'],
                     dicionario['tesesDissertacoes'][i]['dataDefesa'], dicionario['tesesDissertacoes'][i]['titulo'],
                     dicionario['tesesDissertacoes'][i]['autor'], dicionario['tesesDissertacoes'][i]['biblioteca'],
                     dicionario['tesesDissertacoes'][i]['paginas'], dicionario['tesesDissertacoes'][i]['grauAcademico'],
                     dicionario['tesesDissertacoes'][i]['volumes'], dicionario["tesesDissertacoes"][i]["link"]])

    with sqlite3.connect("tesesDissertacoes.db") as conexao:
        with closing(conexao.cursor()) as cursor:
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
                                   num_volumes,
                                   link)
                               values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                               """,
                               dados)
            conexao.commit()
            print("Dados inseridos com sucesso com sucesso!")

#for indice in range(40, 45):
insere_dados(46)
print(46)
#time.sleep(10)
