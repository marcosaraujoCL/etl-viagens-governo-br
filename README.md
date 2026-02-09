# 📊 Pipeline ETL - Viagens do Governo Federal (2025)

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)

> **Resumo:** Script de ETL (*Extract, Transform, Load*) para automatizar o tratamento de dados públicos de viagens do Governo Federal. O projeto transforma dados brutos em um dashboard estratégico para monitoramento de gastos (R$ 14 Bi+), eficiência e geolocalização.

---

## 📷 Demonstração do Dashboard

O painel foi desenvolvido com **Dark Mode** para reduzir a fadiga visual e destacar os KPIs. Utiliza **Mapas de Calor** (Azure Maps) para destinos e implementa análises de **Pareto** (foco nos maiores gastos por ministério, ex: MEC e MJSP).

<div align="center">
  <img src="https://github.com/user-attachments/assets/257fdf56-735b-4097-ab28-db576847ff49" width="100%" alt="Demonstração do Dashboard - Viagens Governo" />
  <p><em>(Aguarde o carregamento do GIF para visualizar a interatividade e os filtros dinâmicos)</em></p>
</div>

---

## 🚀 Tecnologias Utilizadas

* **Python 3.10+:** Script principal de Engenharia de Dados.
* **Pandas:** Biblioteca core para manipulação, limpeza e tipagem do DataFrame.
* **Zipfile & io:** Manipulação eficiente de arquivos compactados em memória (`BytesIO`), sem extração física em disco.
* **Power BI:** Modelagem de Dados, medidas DAX, visualização geográfica e storytelling.

---

## ⚙️ O Processo ETL (Engenharia de Dados)

O script `ETL.py` foi desenhado para ser performático e garantir a integridade dos dados financeiros, executando as seguintes etapas críticas:

### 1️⃣ Extração (Extract)
* 📥 **Leitura Direta:** Processamento de arquivos `.zip` diretamente da fonte ou local, sem necessidade de descompactação manual.
* 🚀 **Otimização de Memória:** Uso da biblioteca `io` para leitura de streams de bytes, acelerando o carregamento inicial.

### 2️⃣ Transformação (Transform)
Nesta etapa, os dados brutos são higienizados para garantir consistência analítica e evitar erros de cálculo:

* 💰 **Limpeza Monetária:** As colunas de valores (Passagens, Diárias) são convertidas do padrão brasileiro (string com vírgula) para `float` numérico, habilitando a soma correta dos **R$ 14 Bilhões**.
* 📝 **Normalização de Texto:** Colunas categóricas (Órgãos, Motivos) são convertidas para **UPPERCASE** e higienizadas com `strip()` para remover espaços fantasmas.
* 📅 **Sazonalidade:** Tratamento de datas para permitir a análise temporal (identificando picos entre agosto e novembro).
* 🆔 **Tipagem Forte:** Garantia de que IDs e CPFs sejam tratados como **Texto** para preservar os zeros à esquerda, essenciais para chaves primárias.

### 3️⃣ Carga (Load)
* 💾 **Exportação Final:** Geração de um arquivo `.csv` otimizado e limpo.
* ✅ **Compatibilidade:** Uso do encoding `utf-8-sig` para leitura perfeita de acentuação no Power BI e Excel.

---

### 👨‍💻 Autor

**Marcos Costa**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](LINK_DO_SEU_LINKEDIN)
[![Portfolio](https://img.shields.io/badge/Portfólio-100000?style=for-the-badge&logo=github&logoColor=white)](LINK_DO_SEU_PORTFOLIO)
