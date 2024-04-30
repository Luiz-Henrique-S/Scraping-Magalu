import requests
from bs4 import BeautifulSoup

def extrair_dados_pagina(url:str):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    }

    dic_produtos = {'titulo': [], 'preco': []}

    # Loop para iterar sobre as paginas
    for pagina in range(1, 4):
        pagina_url = f"{url}?page={pagina}"
        site = requests.get(pagina_url, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')

        # Encontrar todos os produtos da página
        produtos = soup.find_all('a', {'data-testid': 'product-card-container'})

        # Loop para iterar sobre todos os produtos encontrados na página
        for produto in produtos:
            # Extrair título
            titulo_elemento = produto.find('h2', {'data-testid': 'product-title'})
            # Extrair preço
            preco_elemento = produto.find('p', {'data-testid': 'price-value'})

            # Verificar se título e preço foram encontrados
            if titulo_elemento and preco_elemento:
                # Remover caracteres indesejados
                titulo_texto = titulo_elemento.text.strip().split('(')[0].strip()
                preco_texto = preco_elemento.text.strip()
                # Converter o preço para um número float
                preco_numero = float(preco_texto.replace('R$', '').replace('.', '').replace(',', '.'))

                # Verificar se o preço está entre R$ 500 e R$ 7000
                if 500 <= preco_numero <= 7000:
                    dic_produtos['titulo'].append(titulo_texto)
                    dic_produtos['preco'].append(preco_texto)

    return dic_produtos
