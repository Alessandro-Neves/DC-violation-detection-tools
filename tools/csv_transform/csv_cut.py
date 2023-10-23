import pandas as pd
import random

# Carrega o arquivo CSV
nome_arquivo_entrada = 'testdatas/original_datasets/AdultFull.csv'
nome_arquivo_saida = 'testdatas/original_datasets/AdultFull1000.csv'

n_linhas_aleatorias = 10000  # Número de linhas aleatórias a serem selecionadas

# Carrega o arquivo CSV para um DataFrame
dataframe = pd.read_csv(nome_arquivo_entrada)

# Seleciona aleatoriamente n linhas do DataFrame
linhas_aleatorias = random.sample(range(len(dataframe)), n_linhas_aleatorias)
dataframe_aleatorio = dataframe.iloc[linhas_aleatorias]

# Salva as linhas aleatórias em um novo arquivo CSV
dataframe_aleatorio.to_csv(nome_arquivo_saida, index=False)