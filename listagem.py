import sqlite3


lista_final = []

with sqlite3.connect("tesesDissertacoes.db") as conexao:
    for registro in conexao.execute("""select instituicao, programa, autor_trabalho, 
                                              titulo_trabalho, data_defesa, link 
                                      from tesesDissertacoes 
                                      order by programa"""):
        lista_intermediaria = []
        for r in registro:
            lista_intermediaria.append(r.lower())
        lista_final.append(lista_intermediaria)

for item in lista_final:
    print('; '.join(item))

with open('arquivoOutput.csv', 'w') as file:
    file.writelines('instituicao; nomePrograma; autor; titulo; dataDefesa; link' + '\n')
    for item in lista_final:
        file.writelines('; '.join(item) + '\n')
