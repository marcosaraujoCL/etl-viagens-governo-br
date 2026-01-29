# 📊 Pipeline ETL - Viagens do Governo Federal (2025)

Este projeto consiste em um script de **ETL (Extract, Transform, Load)** desenvolvido em Python para automatizar o tratamento de dados públicos de viagens a serviço do Governo Federal.

O objetivo final é gerar uma base de dados limpa e padronizada para alimentar um **Dashboard no Power BI**, permitindo análises de gastos públicos, destinos mais frequentes e motivos de viagens.

## 🚀 Tecnologias Utilizadas

* **Python 3.13**
* **Pandas** (Manipulação e limpeza de dados)
* **Zipfile & io** (Manipulação de arquivos compactados em memória)
* **Power BI** (Visualização dos dados - etapa final)

## ⚙️ O Processo ETL

O script `ETL.py` executa as seguintes etapas:

### 1. Extração (Extract)
* Leitura direta de arquivos `.zip` sem necessidade de descompactação manual.
* Carregamento do arquivo CSV (`2025_Viagem.csv`) utilizando `io.BytesIO` para otimização de memória.
* Tratamento de encoding (`iso-8859-1`) para suportar caracteres da língua portuguesa.

### 2. Transformação (Transform)
Nesta etapa, os dados brutos são higienizados:
* **Conversão Monetária:** As colunas de valores (Passagens, Diárias, etc.) são convertidas do formato brasileiro (1.000,00) para o formato float padrão do Python (1000.00).
* **Padronização de Texto:** Colunas categóricas (como Cargos, Destinos e Motivos) são convertidas para maiúsculas (`UPPERCASE`) e têm espaços extras removidos (`strip`), garantindo consistência nos filtros do Power BI.
* **Datas:** Conversão das colunas de início e fim da viagem para o formato `datetime` (considerando o padrão brasileiro `dayfirst=True`).
* **Identificadores:** IDs como CPF, PCDP e Códigos de Órgãos são convertidos para Texto para preservar zeros à esquerda e evitar formatação numérica incorreta.

### 3. Carga (Load)
* Exportação dos dados tratados para um novo arquivo: `Viagens_Tratadas_Final.csv`.
* Uso do encoding `utf-8-sig` para garantir que acentos e caracteres especiais sejam lidos corretamente pelo **Excel** e **Power BI**.

## 🛠️ Como executar

1. Clone este repositório:
   ```bash
   git clone [https://github.com/marcosaraujoCL/etl-viagens-governo-br.git](https://github.com/marcosaraujoCL/etl-viagens-governo-br.git)