import requests
import json
import sqlite3
from contextlib import closing


URL = 'http://bancodeteses.capes.gov.br/banco-teses/rest/busca'
HEADERS = {'Content-type': 'application/json', 'Accept': 'text/plain'}
DATA = {
    'termo': '"Epistemologia Genética" or "Psicologia Genética" or Piaget',
    'registrosPorPágina': 20
}

payload = DATA.copy()
payload['pagina'] = 1

response = requests.post(URL, headers=HEADERS, data=json.dumps(payload))
print(response.status_code)
if 200 <= response.status_code < 300:
    print(response.json())







"""
dados = []

cabecalho = {'Content-type': 'application/json', 'Accept': 'text/plain'}
payload = {'termo': '"Epistemologia Genética" "Psicologia Genética" Piaget', 'filtros': [],
           'pagina': 1, 'registrosPorPagina': 20}

r = requests.post('http://bancodeteses.capes.gov.br/banco-teses/rest/busca',
                  headers = cabecalho, data = json.dumps(payload))

dicionario = json.loads(r.text)

print(dicionario['total'])


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
"""

