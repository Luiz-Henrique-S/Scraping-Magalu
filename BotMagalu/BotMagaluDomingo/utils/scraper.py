import requests
from bs4 import BeautifulSoup
import re

# funçao para extrair dados de titulo e texto da pagina com argumento "URL"
def extrair_dados_pagina(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    }

    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    
    # Encontrar todos os produtos da pagina
    produtos = soup.find_all('a', {'data-testid': re.compile('product-card-container')})

    #Armazenar titulo e preço dos produtos extraidos
    dic_produtos = {'titulo': [], 'preco': []}

    # Loop para iterar sobre todos os produtos encontrados na pagina
    for produto in produtos:
        # Extrair titulo
        titulo_elemento = produto.find('h2', {'data-testid': re.compile('product-title')})
        # Extrir preço
        preco_elemento = produto.find('p', {'data-testid': re.compile('price-value')})

        # Verifica se título e preço foram encontrados
        if titulo_elemento and preco_elemento: 
            # Remover caracteres indesejados
            titulo_texto = titulo_elemento.text.strip().split('(')[0].strip()
            preco_texto = preco_elemento.text.strip()
            # Converter o preço para um número float
            preco_numero = float(preco_texto.replace('R$', '').replace('.', '').replace(',', '.'))

            # Verificar se o preço está entre R$ 500 e R% 7000
            if 500 <= preco_numero <= 7000:
                dic_produtos['titulo'].append(titulo_texto)
                dic_produtos['preco'].append(preco_texto)
    # retornar os produtos na faixa de preço desejada para o dicionario
    return dic_produtos
