# Import extraction functions for each data source
from extract_selic import selic_to_csv
from extract_ipca import ipca_to_csv
from extract_unemployment import unemployment_to_csv
from extract_debt_to_gdp import debt_to_gdp_to_csv
from extract_igpm import igpm_to_csv
from extract_exchange_rate import exchange_rate_to_csv


import load_to_sql
import transform
import data_quality
import os
from dotenv import load_dotenv
import pandas as pd


# Load environment variables
load_dotenv()

def extract_all():

    os.makedirs("data/raw", exist_ok=True)
    os.makedirs("data/processed", exist_ok=True)

    # Step 1: Extract data from each public API and save as raw CSV
    selic_to_csv()
    ipca_to_csv()
    unemployment_to_csv()
    debt_to_gdp_to_csv()
    igpm_to_csv()
    exchange_rate_to_csv()

def transform_all():
    # Step 3: Transform each raw CSV file and save cleaned versions to the processed layer
    transform.transform_ipca()
    transform.transform_selic()
    transform.transform_unemployment()
    transform.transform_igpm()
    transform.transform_exchange_rate()
    transform.transform_gdp()
    

def validate_all():
    # Step 4: Run data quality checks on each processed CSV file
    data_quality.validate(pd.read_csv(os.getenv("FILE_PATH_IPCA_PROCESSED")), "IPCA")
    data_quality.validate(pd.read_csv(os.getenv("FILE_PATH_SELIC_PROCESSED")), "Selic")
    data_quality.validate(pd.read_csv(os.getenv("FILE_PATH_UNEMPLOYMENT_PROCESSED")), "Unemployment")
    data_quality.validate(pd.read_csv(os.getenv("FILE_PATH_IGPM_PROCESSED")), "IGPM")
    data_quality.validate(pd.read_csv(os.getenv("FILE_PATH_EXCHANGE_RATE_PROCESSED")), "Exchange Rate")
    data_quality.validate(pd.read_csv(os.getenv("FILE_PATH_GDP_PROCESSED")), "GDP")


if __name__ == "__main__":
    # Run the full extraction + upload pipeline
    extract_all()

    # Run the full transformation pipeline
    transform_all()

    # Run the full validation pipeline
    validate_all()

    transform.create_unified_table()

    load_to_sql.load_to_sql()

