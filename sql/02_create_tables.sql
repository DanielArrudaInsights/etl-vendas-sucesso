-- PASSO 2: Criar a estrutura das Tabelas
-- Executar estes comandos dentro do banco 'db_vendas_sucesso'

-- Tabela de Dimensão: Armazena dados que não mudam com frequência
CREATE TABLE IF NOT EXISTS produtos (
    id_produto INT PRIMARY KEY, -- Chave primária: garante que não existam IDs duplicados
    nome VARCHAR(100),          -- Nome do produto (Texto até 100 caracteres)
    setor VARCHAR(50)           -- Categoria (Texto até 50 caracteres)
);

-- Tabela de Fatos: Armazena os eventos (vendas) que acontecem no dia a dia
CREATE TABLE IF NOT EXISTS vendas (
    id_venda INT PRIMARY KEY,    -- Identificador único da venda
    id_produto INT REFERENCES produtos(id_produto), -- Chave estrangeira: liga a venda ao produto
    valor DECIMAL(10, 2),        -- Valor monetário: 10 dígitos no total, sendo 2 decimais
    status VARCHAR(50)           -- Situação da venda (ex: Entregue, Cancelado)
);
