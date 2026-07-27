# 🇧🇷 Brazilian Economic Indicators — Data Pipeline

End-to-end data pipeline that automatically collects, transforms, validates,
and visualizes key Brazilian economic indicators using public APIs,
Apache Airflow, Docker, and Power BI.

---

## About the Project

Economic data in Brazil is scattered across multiple government sources,
requires manual collection, and takes days to consolidate. This pipeline
automates the entire process — from raw API extraction to a ready-to-use
Power BI dashboard — following industry-standard practices like
Medallion Architecture (Bronze/Silver/Gold layers) and orchestrated ETL pipelines.

**Indicators tracked:**
- IPCA (Inflation) — IBGE
- Selic Rate (Interest Rate) — Banco Central do Brasil
- Unemployment Rate (PNAD Contínua) — IBGE
- IGP-M (Market Inflation Index) — Banco Central do Brasil
- USD/BRL Exchange Rate — Banco Central do Brasil
- Debt-to-GDP Ratio — Banco Central do Brasil

---

## Architecture

Public APIs (IBGE + BCB)
↓
Python Scripts (Extract)
↓
Local Storage (CSV)
├── data/raw/ ← Bronze Layer (untouched data)
└── data/processed/ ← Silver Layer (cleaned & validated data)
↓
Python Scripts (Transform + Data Quality)
↓
PostgreSQL (Docker) ← Gold Layer (analytics-ready)
↓
Power BI Dashboard


All steps orchestrated by **Apache Airflow**, running in **Docker**.

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.12 |
| Data Manipulation | Pandas |
| Orchestration | Apache Airflow 2.9 |
| Containerization | Docker + Docker Compose |
| Database | PostgreSQL (Docker) |
| Data Quality | Custom assertions (data_quality.py) |
| Visualization | Power BI Desktop |
| Version Control | Git + GitHub |
| Security | python-dotenv (.env) |

---

## Project Structure

p06_pipeline_economia_br/
│
├── airflow/
│ └── dags/
│ └── pipeline_economia.py # Airflow DAG — orchestrates all tasks
│
├── scripts/
│ ├── extract_ipca.py # Extracts IPCA from IBGE API
│ ├── extract_selic.py # Extracts Selic from BCB API
│ ├── extract_unemployment.py # Extracts unemployment from IBGE API
│ ├── extract_igpm.py # Extracts IGP-M from BCB API
│ ├── extract_exchange_rate.py # Extracts USD/BRL from BCB API
│ ├── extract_debt_to_gdp.py # Extracts Debt/GDP from BCB API
│ ├── transform.py # Cleans, standardizes and unifies data
│ ├── data_quality.py # Validates nulls, duplicates and empty sets
│ ├── load_to_sql.py # Loads unified data into PostgreSQL
│ └── main.py # Entry point — orchestrates full pipeline
│
├── data/
│ ├── raw/ # Bronze layer (raw CSVs)
│ └── processed/ # Silver layer (cleaned CSVs)
│
├── docker-compose-airflow.yml # Airflow + PostgreSQL Docker setup
├── .env # Credentials and file paths (not committed)
├── .gitignore
└── README.md


---

## DAG — Airflow Pipeline

The pipeline runs daily at 08:00 UTC with the following task sequence:

extract_and_upload → transform → validate → create_unified_table → load_to_sql


---

## How to Run

### Prerequisites
- Docker Desktop installed and running
- Python 3.12+

### 1. Clone the repository
```bash
git clone https://github.com/joao07vitor05/pipeline-economia-br.git
cd pipeline-economia-br
```

### 2. Create the `.env` file
```env
FILE_PATH_IPCA=data/raw/ipca.csv
FILE_PATH_SELIC=data/raw/selic.csv
FILE_PATH_UNEMPLOYMENT=data/raw/unemployment.csv
FILE_PATH_IGPM=data/raw/igpm.csv
FILE_PATH_EXCHANGE_RATE=data/raw/exchange_rate.csv
FILE_PATH_GDP=data/raw/debt_to_gdp.csv

FILE_PATH_IPCA_PROCESSED=data/processed/ipca.csv
FILE_PATH_SELIC_PROCESSED=data/processed/selic.csv
FILE_PATH_UNEMPLOYMENT_PROCESSED=data/processed/unemployment.csv
FILE_PATH_IGPM_PROCESSED=data/processed/igpm.csv
FILE_PATH_EXCHANGE_RATE_PROCESSED=data/processed/exchange_rate.csv
FILE_PATH_GDP_PROCESSED=data/processed/debt_to_gdp.csv
FILE_PATH_UNIFIED_TABLE=data/processed/economic_indicators.csv

POSTGRES_HOST=postgres
POSTGRES_PORT=5432
POSTGRES_DB=your_db
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
```

### 3. Start Airflow and PostgreSQL
```bash
docker-compose -f docker-compose-airflow.yml up -d
```

### 4. Access the Airflow UI

http://localhost:8080
user: admin | password: admin


Activate the `pipeline_economia_br` DAG and trigger it manually.

---

## Data Quality

Every indicator is validated after transformation with three checks:
- ✅ DataFrame is not empty
- ✅ No null values
- ✅ No duplicate rows

---

## Dashboard

Built in Power BI Desktop, connected directly to PostgreSQL database.

**Page 1 — Visão Geral e Correlações:** 
* **KPI Cards:** Latest metric values (IPCA, Selic, Câmbio, Dívida/PIB, IGP-M, Desemprego) with sparkline trends.
* **Macro Correlations:** Multi-indicator time series charts comparing Selic x IPCA x IGP-M and PIB x Taxa de Desemprego.

**Page 2 — Análise dos Indicadores Econômicos (Deep Dive):** 
* **Interactive Selector:** Allows dynamic filtering by economic indicator (e.g., Câmbio, IPCA, Selic).
* **Summary & Stats:** Key statistical metrics (Latest Value, Average, Max, Standard Deviation) alongside a qualitative summary table (Status, Trend, Volatility).
* **Historical Analysis:** Normalized historical evolution chart and annual percentage variation bar chart.

---

## Security

All credentials are stored in a `.env` file never committed to GitHub.
No API keys required — all data sources are public and free.

---

## Author

João Vitor — [LinkedIn](https://www.linkedin.com/in/joaovitorgomesoliveira/) | [GitHub](https://github.com/joao07vitor05)