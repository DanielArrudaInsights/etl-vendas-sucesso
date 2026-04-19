import pandas as pd
from sqlalchemy import create_engine

# Configurações de conexão (As mesmas que você usou no carregar_banco.py)
USUARIO = 'postgres'
SENHA = 'Sua_senha_aqui'
HOST = 'localhost'
PORTA = '5432'
BANCO = 'db_vendas_sucesso'

try:
    # 1. Criar a conexão com o banco de dados
    engine = create_engine(f'postgresql://{USUARIO}:{SENHA}@{HOST}:{PORTA}/{BANCO}')
    
    # 2. Extrair os dados brutos usando uma Query SQL
    print(" Coletando dados do banco para análise...")
    query = """
    SELECT p.setor, v.valor 
    FROM vendas v 
    JOIN produtos p ON v.id_produto = p.id_produto
    """
    df = pd.read_sql(query, engine)
    
    # 3. Transformação com Pandas: Agrupar por setor e somar o faturamento
    print(" Calculando faturamento por setor...")
    relatorio = df.groupby('setor')['valor'].sum().reset_index()
    relatorio.columns = ['Setor', 'Faturamento_Total']
    
    # 4. Salvar o resultado final em um novo CSV (Relatório de Negócio)
    relatorio.to_csv('data/relatorio_faturamento.csv', index=False, encoding='utf-8')
    
    print("\n RELATÓRIO DE FATURAMENTO GERADO COM SUCESSO!")
    print(relatorio)

except Exception as e:
    print(f" Erro na transformação: {e}")