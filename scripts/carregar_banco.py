import pandas as pd
from sqlalchemy import create_engine

# Configurações de conexão
# Formato: postgresql://usuario:senha@localhost:porta/nome_do_banco
USUARIO = 'postgres'
SENHA = 'sua_senha_aqui'
HOST = 'localhost'
PORTA = '5432'
BANCO = 'db_vendas_sucesso'

try:
    # 1. Criar conexão com o banco
    engine = create_engine(f'postgresql://{USUARIO}:{SENHA}@{HOST}:{PORTA}/{BANCO}')
    
    # 2. Carregar produtos
    print(" Carregando produtos...")
    df_p = pd.read_csv('data/produtos.csv', encoding='utf-8')
    df_p.to_sql('produtos', engine, if_exists='append', index=False)
    
    # 3. Carregar vendas
    print(" Carregando vendas...")
    df_v = pd.read_csv('data/vendas.csv', encoding='utf-8')
    df_v.to_sql('vendas', engine, if_exists='append', index=False)

    print("\n PROJETO CONCLUÍDO! Dados inseridos no PostgreSQL com sucesso.")

except Exception as e:
    print(f"\n Erro durante a carga: {e}")
    print("Dica: Verifique se as tabelas já foram criadas no pgAdmin e se a senha está correta.")