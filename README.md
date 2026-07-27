# 🇧🇷 Brazilian Economic Indicators — Data Pipeline

End-to-end data pipeline that automatically collects, transforms, 
and visualizes key Brazilian economic indicators using public APIs, 
Azure cloud infrastructure, and Power BI.

---

##  About the Project

This project was built to solve a common problem in Brazilian companies: 
economic data is scattered across multiple government sources, requires 
manual collection, and takes days to consolidate.

This pipeline automates the entire process — from raw API data to 
a ready-to-use dashboard — following industry-standard practices 
like Medallion Architecture (Bronze/Silver/Gold layers) and ETL pipelines.

**Indicators tracked:**
- IPCA (Inflation) — IBGE
- Selic Rate (Interest Rate) — Banco Central do Brasil
- Unemployment Rate (PNAD) — IBGE
- IGP-M (Market Inflation Index) — Banco Central do Brasil
- USD/BRL Exchange Rate — Banco Central do Brasil
- Debt-to-GDP Ratio — Banco Central do Brasil

---

##  Architecture
Public APIs (IBGE + BCB)

↓

Python Scripts (Extract)

↓

Azure Data Lake Storage Gen2

├── raw/          ← Bronze Layer (untouched data)

└── processed/    ← Silver Layer (cleaned data)

↓

Python Scripts (Transform)

↓

Azure SQL Database    ← Gold Layer (analytics-ready)

↓

Power BI Dashboard

---

##  Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.12 |
| Data Manipulation | Pandas |
| Cloud Storage | Azure Data Lake Storage Gen2 |
| Database | Azure SQL Database (Serverless) |
| Orchestration | main.py (local) |
| Visualization | Power BI Desktop |
| Version Control | Git + GitHub |
| Security | python-dotenv (.env) |

---

##  Project Structure
pipeline-economia-br/

│

├── scripts/

│   ├── extract_ipca.py          # Extracts IPCA data from IBGE API

│   ├── extract_selic.py         # Extracts Selic rate from BCB API

│   ├── extract_unemployment.py  # Extracts unemployment from IBGE API

│   ├── extract_igpm.py          # Extracts IGP-M from BCB API

│   ├── extract_usd_brl.py       # Extracts USD/BRL rate from BCB API

│   ├── extract_debt_to_gdp.py   # Extracts Debt/GDP from BCB API

│   ├── transform.py             # ETL — cleans and unifies all data

│   ├── upload_azure.py          # Uploads files to Azure Data Lake

│   ├── load_to_sql.py           # Loads data into Azure SQL Database

│   └── main.py                  # Orchestrates the full pipeline

│

├── .gitignore

└── README.md

---

##  How to Run

1. Clone the repository
```bash
git clone https://github.com/joao07vitor05/pipeline-economia-br.git
```

2. Install dependencies
```bash
pip install requests pandas azure-storage-blob python-dotenv sqlalchemy pyodbc
```

3. Create a `.env` file in the root with your credentials:
AZURE_CONNECTION_STRING=your_azure_connection_string

SQL_CONNECTION_STRING=your_sql_connection_string

FILE_PATH_IPCA=data/raw/ipca.csv
... (see .env.example for full list)

4. Run the full pipeline
```bash
python scripts/main.py
python scripts/transform.py
python scripts/load_to_sql.py
```

---

##  Security

All credentials are stored in a `.env` file that is **never committed 
to GitHub** (listed in `.gitignore`). No API keys are required — 
all data sources are public and free.

---

##  Dashboard

Built in Power BI Desktop, connected directly to Azure SQL Database.

*(screenshot coming soon)*

---

##  Author

João Vitor — [LinkedIn](https://www.linkedin.com/in/joaovitorgomesoliveira/) | [GitHub](https://github.com/joao07vitor05)