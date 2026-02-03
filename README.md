# 📊 Pipeline ETL - Viagens do Governo Federal (2025)

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)

> **Resumo:** Script de ETL (Extract, Transform, Load) para automatizar o tratamento de dados públicos de viagens a serviço do Governo Federal, gerando insights sobre gastos e eficiência.

---

## 📷 Demonstração do Dashboard

O painel utiliza **Dark Mode** para foco em análise, **Mapas de Calor** (Azure Maps) para geolocalização e **Matrizes Hierárquicas** para detalhamento.

<div align="center">
  <img src="https://github.com/user-attachments/assets/5c57d502-e154-4c5f-8c2c-051d9c424d26" width="100%" alt="Demonstração do Dashboard" />
  <p><em>(Aguarde o carregamento do GIF para visualizar a interatividade)</em></p>
</div>

---

## 🚀 Tecnologias Utilizadas

* **Python 3.13:** Script principal de Engenharia de Dados.
* **Pandas:** Biblioteca core para manipulação e limpeza do DataFrame.
* **Zipfile & io:** Manipulação eficiente de arquivos compactados em memória (sem extração física).
* **Power BI:** Modelagem de Dados, medidas DAX e Visualização interativa.

---

## ⚙️ O Processo ETL (Engenharia de Dados)

O script `ETL.py` foi desenhado para ser eficiente e escalável, executando as seguintes etapas críticas:

### 1️⃣ Extração (Extract)
* 📥 **Leitura Direta:** Processamento de arquivos `.zip` sem necessidade de descompactação manual, economizando armazenamento.
* 🚀 **Otimização de Memória:** Carregamento do `2025_Viagem.csv` utilizando `io.BytesIO`.
* 🔤 **Encoding:** Tratamento de codificação (`iso-8859-1`) para garantir a integridade de acentos e caracteres especiais.

### 2️⃣ Transformação (Transform)
Nesta etapa, os dados brutos são higienizados para garantir consistência analítica:

* 💰 **Conversão Monetária:** As colunas de valores (Passagens, Diárias) são convertidas do padrão brasileiro (ex: `1.000,00`) para `float` (ex: `1000.00`), habilitando cálculos matemáticos.
* 📝 **Padronização de Texto:** Colunas categóricas (Cargos, Destinos, Motivos) são normalizadas para **UPPERCASE** e higienizadas com `strip()`, garantindo filtros precisos no Power BI.
* 📅 **Datas:** Conversão de strings para objetos `datetime` (padrão `dayfirst=True`), permitindo cálculo de duração das viagens.
* 🆔 **Identificadores:** IDs críticos (CPF, PCDP, Códigos de Órgãos) são convertidos para **Texto** para preservar zeros à esquerda.

### 3️⃣ Carga (Load)
* 💾 **Exportação Final:** Geração do arquivo `Viagens_Tratadas_Final.csv` pronto para consumo.
* ✅ **Compatibilidade:** Uso do encoding `utf-8-sig` para leitura perfeita no Power BI e Excel.

---
Autor: Marcos Costa
