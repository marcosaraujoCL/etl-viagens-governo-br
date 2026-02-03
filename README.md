📊 Pipeline ETL - Viagens do Governo Federal (2025)
Este projeto consiste em um script de ETL (Extract, Transform, Load) desenvolvido em Python para automatizar o tratamento de dados públicos de viagens a serviço do Governo Federal.

O objetivo final é gerar uma base de dados limpa e padronizada para alimentar um Dashboard no Power BI, permitindo auditoria de gastos, identificação de gargalos e análise de eficiência.

📷 Demonstração do Dashboard
Destaque: O painel utiliza Dark Mode para foco em análise, Mapas de Calor (Azure Maps) para geolocalização de gastos e Matrizes Hierárquicas para detalhamento de despesas.

!(img/Animação.gif) (Aguarde o carregamento do GIF para visualizar a interatividade)

🚀 Tecnologias Utilizadas
Python 3.13 (Script de Engenharia de Dados)

Pandas (Manipulação e limpeza de dados)

Zipfile & io (Manipulação de arquivos compactados em memória)

Power BI (Modelagem de Dados, DAX e Visualização)

⚙️ O Processo ETL (Engenharia)
O script ETL.py executa as seguintes etapas críticas:

1. Extração (Extract)
Leitura direta de arquivos .zip sem necessidade de descompactação manual, economizando armazenamento local.

Carregamento do arquivo CSV (2025_Viagem.csv) utilizando io.BytesIO para otimização de memória.

Tratamento de encoding (iso-8859-1) para garantir a integridade de caracteres da língua portuguesa.

2. Transformação (Transform)
Nesta etapa, os dados brutos são higienizados para análise:

Conversão Monetária: As colunas de valores (Passagens, Diárias, etc.) são convertidas do formato brasileiro (ex: 1.000,00) para o formato float padrão do Python (1000.00), permitindo cálculos matemáticos.

Padronização de Texto: Colunas categóricas (como Cargos, Destinos e Motivos) são normalizadas para maiúsculas (UPPERCASE) e têm espaços extras removidos (strip), garantindo consistência nos filtros do Power BI.

Datas: Conversão das colunas de início e fim da viagem para o formato datetime (considerando o padrão dayfirst=True), permitindo cálculos de duração.

Identificadores: IDs como CPF, PCDP e Códigos de Órgãos são convertidos para Texto para preservar zeros à esquerda e evitar formatação numérica incorreta.

3. Carga (Load)
Exportação dos dados tratados para um novo arquivo: Viagens_Tratadas_Final.csv.

Uso do encoding utf-8-sig para garantir compatibilidade total com o motor do Power BI e Excel.

📊 Funcionalidades do Dashboard (Analytics)
O arquivo Dashboard_Viagens.pbix disponível neste repositório contém:

Mapa de Calor Global: Visualização de densidade que destaca instantaneamente os países e cidades com maior volume de gastos.

Análise de Urgência: Filtro dinâmico que permite isolar "Viagens Urgentes" para auditar custos elevados por falta de planejamento.

Ranking de Órgãos: Utilização de Árvore de Decomposição (ou Matriz) para explorar quais ministérios gastam mais e os motivos específicos de cada despesa.

KPIs Financeiros: Medidas DAX para cálculo de Ticket Médio, Total Gasto e Percentual de Urgência.

🛠️ Como executar este projeto
Pré-requisitos
Python 3.x instalado.

Power BI Desktop instalado.

Passo a passo
Clone este repositório:bash git clone https://github.com/marcosaraujoCL/etl-viagens-governo-br.git

Instale as dependências do Python:

Bash
pip install pandas
Execute o script de ETL:

Bash
python ETL.py
Abra o arquivo .pbix no Power BI e atualize os dados apontando para o novo CSV gerado.

Autor: Marcos Costa