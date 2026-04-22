# Projeto ETL: Inteligência e Performance de Vendas (Vendas Sucesso)

Este repositório apresenta um pipeline de dados completo (ETL) que simula a operação real de uma empresa de varejo. O foco aqui não é apenas o código, mas a garantia da **integridade dos dados** e a geração de **insights estratégicos** para a tomada de decisão.

## Insights Gerados pelo Projeto
Abaixo estão os principais pontos de valor que este pipeline entrega para a área de negócios:

* **Saneamento Automatizado:** O sistema detecta e resolve conflitos de codificação (`UTF-8` vs `Latin1`), garantindo que nomes de produtos e cidades brasileiras não fiquem corrompidos no banco de dados.
* **Visão de Faturamento por Setor:** O script de transformação consolida milhares de linhas de vendas brutas em métricas claras de performance por categoria de produto.
* **Eficiência em Larga Escala:** Utilização de `SQLAlchemy` e carregamento em blocos (*chunks*), permitindo que o processo seja escalável para milhões de registros sem travar a memória.
* **Auditabilidade:** Estrutura de banco de dados em esquema Estrela (*Star Schema*), facilitando a conexão com ferramentas de BI como Power BI e Tableau.

---

## Tecnologias Utilizadas
* **Python 3.x** (Processamento e Lógica)
* **Pandas** (Transformação e Limpeza)
* **PostgreSQL** (Armazenamento Robusto)
* **SQLAlchemy** (Interface Banco-Aplicação)

---

## Estrutura Técnica e Implementação

### 1. Modelagem do Banco de Dados
Para suportar o ambiente brasileiro e evitar erros de caracteres enfrentados em versões anteriores, o banco foi configurado com localidade específica:

```sql
-- Criação do banco com suporte a caracteres brasileiros
CREATE DATABASE db_vendas_sucesso
WITH ENCODING = 'UTF8'
LC_COLLATE = 'Portuguese_Brazil.1252'
LC_CTYPE = 'Portuguese_Brazil.1252';

-- Tabela de Fatos: Vendas
CREATE TABLE IF NOT EXISTS vendas (
    id_venda INT PRIMARY KEY,
    id_produto INT REFERENCES produtos(id_produto),
    valor DECIMAL(10, 2),
    data_venda DATE
);