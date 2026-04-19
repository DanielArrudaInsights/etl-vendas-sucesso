# Projeto ETL: Performance de Vendas (Vendas Sucesso)

Este repositório contém um pipeline de dados completo (Extração, Transformação e Carga) desenvolvido como parte dos meus estudos em Banco de Dados e Data Science. O objetivo é simular o fluxo de dados de uma empresa de varejo, garantindo a integridade dos dados e a compatibilidade de caracteres entre o sistema operacional Windows e o banco de dados PostgreSQL.

## Estrutura do Banco de Dados

Para evitar erros de codificação (como o erro de codec `utf-8` enfrentado em versões anteriores), o banco de dados foi configurado com localidade compatível com o ambiente brasileiro.

### 1. Inicialização do Banco
O comando abaixo deve ser executado no pgAdmin (conectado ao banco padrão `postgres`) para criar o ambiente do projeto.

```sql
-- Criação do banco de dados com codificação UTF8
-- Utilizamos a localidade Portuguese_Brazil para garantir compatibilidade com o Windows
CREATE DATABASE db_vendas_sucesso 
WITH ENCODING = 'UTF8' 
LC_COLLATE = 'Portuguese_Brazil.1252' 
LC_CTYPE = 'Portuguese_Brazil.1252';
-- Tabela de Dimensão: produtos
-- Armazena o catálogo de itens. Nomes e setores foram mantidos sem acentos para máxima compatibilidade.
CREATE TABLE IF NOT EXISTS produtos (
    id_produto INT PRIMARY KEY, -- Identificador único do produto (Chave Primária)
    nome VARCHAR(100),          -- Descrição do item
    setor VARCHAR(50)           -- Categoria à qual o produto pertence
);

-- Tabela de Fatos: vendas
-- Registra cada transação realizada e se conecta à tabela de produtos.
CREATE TABLE IF NOT EXISTS vendas (
    id_venda INT PRIMARY KEY,    -- Identificador único da transação
    id_produto INT REFERENCES produtos(id_produto), -- Relacionamento com a tabela produtos (Chave Estrangeira)
    valor DECIMAL(10, 2),        -- Valor da venda com precisão decimal
    status VARCHAR(50)           -- Situação atual (Ex: Entregue, Processando)
);
SELECT 
    v.id_venda, 
    p.nome AS produto, 
    p.setor, 
    v.valor, 
    v.status
FROM vendas v
JOIN produtos p ON v.id_produto = p.id_produto;