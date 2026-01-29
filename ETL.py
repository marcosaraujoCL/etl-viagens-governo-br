# SCRIPT PADRÃO PARA IMPORTAR UMA BASE DE DADOS DE UM ARQUIVO "ZIP" QUE POSSUI MAIS DE UM CSV:
import pandas as pd
from zipfile import ZipFile
import io

# 1. Defini o caminho do meu arquivo ZIP:
caminho_zip = r'C:\Users\Lenovo\Desktop\Projeto 1 (PR)\2025_20260118_Viagens.zip'

# 2. Especifiquei o arquivo CSV que eu vou utilizar dentro do ZIP:
nome_arquivo_csv = '2025_Viagem.csv' 

# 3. Usei o gerenciador de contexto 'with' para abrir o ZIP e o CSV:
with ZipFile(caminho_zip, 'r') as meu_zip:
    # - Com meu outro "With" especifiquei com a função "open" da biblioteca "ZipFile" o CSV que eu vou utilizar e defino com o "arquivo_csv".
    with meu_zip.open(nome_arquivo_csv) as arquivo_csv:
        # - io.BytesIO permite que pandas leia o conteúdo descompactado em memória
        df_origem = pd.read_csv(io.BytesIO(arquivo_csv.read()), sep=';', encoding='iso-8859-1')

# 4. Converto essa colunas para float:
colunas_float = ['Valor passagens', 'Valor diárias', 'Valor outros gastos', 'Valor devolução']

for col in colunas_float:
    # Passo A: Remove ponto de milhar
    df_origem[col] = df_origem[col].str.replace('.', '', regex=False)
    
    # Passo B: Troca vírgula por ponto decimal
    df_origem[col] = df_origem[col].str.replace(',', '.', regex=False)
    
    # Passo C: converto para float
    df_origem[col] = df_origem[col].astype(float)

# 4. Converto essas colunas para texto:
colunas_texto = ['Situação', 'Viagem Urgente', 'Justificativa Urgência Viagem','Nome do órgão superior',
                 'Nome órgão solicitante', 'Nome', 'Cargo', 'Função', 'Descrição Função', 'Destinos', 'Motivo',]

for col in colunas_texto:
    # Padroniza nomes para maiúsculo e remove espaços extras
    df_origem[col] = df_origem[col].str.strip().str.upper()

    # Passo B: converto para texto
    df_origem[col] = df_origem[col].astype(str)

# 5. Converto essas colunas para data:
colunas_datas = ['Período - Data de início', 'Período - Data de fim']

for col in colunas_datas:

    df_origem[col] = pd.to_datetime(df_origem[col], dayfirst=True, errors='coerce')
# 6. converto colunas números para texto: 
colunas_num_text = ['Código do órgão superior', 'Código órgão solicitante', 'CPF viajante', 'Número da Proposta (PCDP)', 'Identificador do processo de viagem']

for col in colunas_num_text:

    df_origem[col] = df_origem[col].astype(str)

# Definindo o nome do arquivo final limpo
caminho_saida = r'C:\Users\Lenovo\Desktop\Projeto 1 (PR)\Viagens_Tratadas_Final.csv'

# Salvamos em CSV. O encoding 'utf-8-sig' é CRUCIAL para o Excel/Power BI lerem acentos corretamente.
# index=False impede que o pandas crie uma coluna extra de numeração.
df_origem.to_csv(caminho_saida, index=False, encoding='utf-8-sig')