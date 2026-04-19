import pandas as pd
import os

# 1. Garantir que a pasta 'data' exista
if not os.path.exists('data'):
    os.makedirs('data')
    print(" Pasta 'data' criada.")

# 2. Criar dados fictícios limpos (sem acentos para evitar erros de encoding)
# Nota: Usamos nomes simples para garantir que o motor funcione 100%
dados_produtos = {
    'id_produto': [1, 2, 3, 4],
    'nome': ['Cadeira Gamer', 'Mesa de Escritorio', 'Luminaria Led', 'Monitor HD'],
    'setor': ['Moveis', 'Moveis', 'Decoracao', 'Eletronicos']
}

dados_vendas = {
    'id_venda': [1001, 1002, 1003, 1004],
    'id_produto': [1, 2, 3, 1],
    'valor': [1250.50, 890.00, 150.90, 1250.50],
    'status': ['Entregue', 'Processando', 'Entregue', 'Cancelado']
}

# 3. Transformar em DataFrames e salvar em CSV
df_produtos = pd.DataFrame(dados_produtos)
df_vendas = pd.DataFrame(dados_vendas)

# Salvando com UTF-8 explícito
df_produtos.to_csv('data/produtos.csv', index=False, encoding='utf-8')
df_vendas.to_csv('data/vendas.csv', index=False, encoding='utf-8')

print(" Arquivos CSV gerados com sucesso na pasta /data!")
