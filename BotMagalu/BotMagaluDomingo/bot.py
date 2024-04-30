import pandas as pd
from utils.scraper import extrair_dados_pagina
from utils.save_planilha import extracao_para_planilha

def main():
    extracao_para_planilha()

#Verifica se o codigo esta sendo executado na função "main"
if __name__ == '__main__':
    main()
