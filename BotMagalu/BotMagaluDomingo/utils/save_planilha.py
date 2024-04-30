import pandas as pd
from utils.scraper import extrair_dados_pagina

def extracao_para_planilha():
    url_celulares = 'https://www.magazineluiza.com.br/busca/celular/'
    url_geladeiras = 'https://www.magazineluiza.com.br/busca/geladeira/'

    dados_celulares = extrair_dados_pagina(url_celulares)
    dados_geladeiras = extrair_dados_pagina(url_geladeiras)

    # Criar DataFrames para celulares e geladeiras
    df_celulares = pd.DataFrame(dados_celulares)
    df_geladeiras = pd.DataFrame(dados_geladeiras)

    # Renomear as colunas de celulares e geladeiras
    df_celulares = df_celulares.rename(columns={'titulo': 'celulares', 'preco': 'preco_celulares'})
    df_geladeiras = df_geladeiras.rename(columns={'titulo': 'geladeiras', 'preco': 'preco_geladeiras'})

    # Juntar os DataFrames de celulares e geladeiras
    df_final = pd.concat([df_celulares, df_geladeiras], axis=1)

    # Selecionar apenas as colunas desejadas
    df_final = df_final[['celulares', 'preco_celulares', 'geladeiras', 'preco_geladeiras']]

    # Salvar o DataFrame como CSV
    df_final.to_csv('produtos_magalu.csv', index=False, sep=';')