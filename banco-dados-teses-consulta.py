import sqlite3

'''
with sqlite3.connect("tesesDissertacoes.db") as conexao:
    conexao.row_factory = sqlite3.Row
    for teses in conexao.execute("select * from tesesDissertacoes where id = 71"):
        print(teses["id"],
              "\nCódigo:", teses["codigo"],
              "\nMunicípio do Programa:", str.lower(teses["municipio"]),
              "\nInstituição do Programa:", str.lower(teses["instituicao"]),
              "\nNome do Programa: ", str.lower(teses["programa"]),
              "\nData da Defesa:", teses["data_defesa"],
              "\nTítulo do Trabalho:", str.lower(teses["titulo_trabalho"]),
              "\nAutor do Trabalho:", str.lower(teses["autor_trabalho"]),
              "\nBiblioteca:", teses["biblioteca"],
              "\nNúmero de páginas:", teses["num_paginas"],
              "\nGrau Acadêmico:", teses["grau_academico"],
              "\nNúmero de Volumes:", teses["num_volumes"],
              "\nLink:", teses["link"],"\n")

'''

with sqlite3.connect("tesesDissertacoes.db") as conexao:
    conexao.row_factory = sqlite3.Row
    for teses in conexao.execute("""
                    select *
                    from tesesDissertacoes
                    where data_defesa > '2007-12-31' and autor_trabalho = 'VICENTE EDUARDO RIBEIRO MARÇAL'
                    """):
        print(teses["id"],
              "\nCódigo:", teses["codigo"],
              "\nMunicípio do Programa:", str.lower(teses["municipio"]),
              "\nInstituição do Programa:", str.lower(teses["instituicao"]),
              "\nNome do Programa: ", str.lower(teses["programa"]),
              "\nData da Defesa:", teses["data_defesa"],
              "\nTítulo do Trabalho:", str.lower(teses["titulo_trabalho"]),
              "\nAutor do Trabalho:", str.lower(teses["autor_trabalho"]),
              "\nBiblioteca:", teses["biblioteca"],
              "\nNúmero de páginas:", teses["num_paginas"],
              "\nGrau Acadêmico:", teses["grau_academico"],
              "\nNúmero de Volumes:", teses["num_volumes"],
              "\nLink:", teses["link"],"\n")
