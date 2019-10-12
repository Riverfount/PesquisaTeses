import math

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

