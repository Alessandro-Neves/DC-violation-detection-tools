import pandas as pd

# Ler o arquivo CSV
nome_arquivo_entrada = '/home/alessandro/Restore/IC-BD-Pena/DC-violation-detection-tools/testdatas/clean_datasets/lineitem_250000.csv'
df = pd.read_csv(nome_arquivo_entrada)

# Verifique se a coluna 'id' existe no DataFrame
if 'id' in df.columns:
    # Remover a coluna 'id'
    df = df.drop(columns=['id'])

# Salvar o DataFrame em um novo arquivo CSV
nome_arquivo_saida = '/home/alessandro/Restore/IC-BD-Pena/DC-violation-detection-tools/testdatas/clean_datasets/lineitem_150000.csv'
df.to_csv(nome_arquivo_saida, index=False)

print(f'Coluna "id" removida e dados salvos em {nome_arquivo_saida}.')
