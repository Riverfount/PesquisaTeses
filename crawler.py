import math
import requests
import json


URL = 'http://bancodeteses.capes.gov.br/banco-teses/rest/busca'
HEADERS = {'Content-type': 'application/json', 'Accept': 'text/plain'}
DATA = {
    'termo': '"Epistemologia Genética" "Psicologia Genética" Piaget',
    'registrosPorPágina': 20
}


def fetch_page(page_number):
    print('Entrei na função fetch_page')
    payload = DATA.copy()
    payload['pagina'] = page_number

    while True:
        response = requests.post(URL, headers = HEADERS, data = json.dumps(payload))

        if 200 <= response.status_code < 300:
            return response.json()
        else:
            print(response.status_code)
            continue


def get_total_pages(response):
    print('Entrei na função get_total_pages')
    total = response['total']
    per_page = response['registrosPorPagina']
    return math.ceil(total / per_page)


if __name__ == '__main__':

    total = 1
    current = 1
    output = []
    print('Vou entrar no while agora')
    while current <= total:
        response = fetch_page(1)

        if current == 1:
            total = get_total_pages(response)

        for dissertation in response['tesesDissertacoes']:
            output.append(dissertation)

        current += 1  # let's go to the next page (the while condition blocks a non-existent page)
        print(current, end = ' ')

    print(output[-1])
