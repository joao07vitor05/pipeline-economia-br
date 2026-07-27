import pandas as pd
from dotenv import load_dotenv 
import os
from data_quality import validate  

# Load environment variables (file paths) from .env
load_dotenv()


def transform_ipca():
    # Read raw IPCA data
    df = pd.read_csv(os.getenv("FILE_PATH_IPCA"))

    # Rename column to a clearer, descriptive name
    df = df.rename(columns={'value': 'inflation_rate'})

    # Convert period from "YYYYMM" format to a proper date
    df['period']= pd.to_datetime(df['period'], format='%Y%m')

    # Add a column to identify the data source/indicator
    df['indicator'] = 'ipca'

    # Save the cleaned data to the processed layer
    df.to_csv(os.getenv("FILE_PATH_IPCA_PROCESSED") , index=False)

    print(df.head(5))

def transform_selic():
    # Read raw Selic data
    df =  pd.read_csv(os.getenv("FILE_PATH_SELIC"))

    # Rename columns from Portuguese to English, descriptive names
    df = df.rename(columns={'data': 'period', 'valor': 'selic_rate'})

    # Convert period from "DD/MM/YYYY" format to a proper date
    df['period'] = pd.to_datetime(df['period'], format='%d/%m/%Y')

    # Add a column to identify the data source/indicator
    df['indicator'] = 'selic'

    # Save the cleaned data to the processed layer
    df.to_csv(os.getenv("FILE_PATH_SELIC_PROCESSED"), index=False)

    print(df.head(5))

def transform_unemployment():
    # Read raw unemployment data
    df = pd.read_csv(os.getenv("FILE_PATH_UNEMPLOYMENT"))

    # Convert period from "YYYYMM" format to a proper date
    df['period'] = pd.to_datetime(df['period'], format='%Y%m')

    # Add a column to identify the data source/indicator
    df['indicator'] = 'unemployment'

    # Save the cleaned data to the processed layer
    df.to_csv(os.getenv("FILE_PATH_UNEMPLOYMENT_PROCESSED"), index=False)
    print(df.head(5))

def transform_igpm():
    # Read raw IGPM data
    df = pd.read_csv(os.getenv("FILE_PATH_IGPM"))

    df = df.rename(columns={'valor': 'igpm_rate', 'data': 'period'})

    # Convert period from "YYYYMM" format to a proper date
    df['period'] = pd.to_datetime(df['period'], format='%d/%m/%Y')

    # Add a column to identify the data source/indicator
    df['indicator'] = 'igpm'

    # Save the cleaned data to the processed layer
    df.to_csv(os.getenv("FILE_PATH_IGPM_PROCESSED"), index=False)
    print(df.head(5))

def transform_exchange_rate():
    # Read raw exchange rate data
    df = pd.read_csv(os.getenv("FILE_PATH_EXCHANGE_RATE"))

    df = df.rename(columns={'valor': 'exchange_rate', 'data': 'period'})

    # Convert period from "YYYYMM" format to a proper date
    df['period'] = pd.to_datetime(df['period'], format='%d/%m/%Y')

    # Add a column to identify the data source/indicator
    df['indicator'] = 'exchange_rate'

    # Save the cleaned data to the processed layer
    df.to_csv(os.getenv("FILE_PATH_EXCHANGE_RATE_PROCESSED"), index=False)
    print(df.head(5))

def transform_gdp():
    # Read raw GDP data
    df = pd.read_csv(os.getenv("FILE_PATH_GDP"))

    df = df.rename(columns={'valor': 'gdp', 'data': 'period'})

    # Convert period from "YYYYMM" format to a proper date
    df['period'] = pd.to_datetime(df['period'], format='%d/%m/%Y')

    # Add a column to identify the data source/indicator
    df['indicator'] = 'gdp'

    # Save the cleaned data to the processed layer
    df.to_csv(os.getenv("FILE_PATH_GDP_PROCESSED"), index=False)
    print(df.head(5))

def create_unified_table():
    # Read each processed (Silver layer) table
    df_ipca = pd.read_csv(os.getenv("FILE_PATH_IPCA_PROCESSED"))
    df_selic = pd.read_csv(os.getenv("FILE_PATH_SELIC_PROCESSED"))
    df_unemployment = pd.read_csv(os.getenv("FILE_PATH_UNEMPLOYMENT_PROCESSED"))
    df_igpm = pd.read_csv(os.getenv("FILE_PATH_IGPM_PROCESSED"))
    df_exchange_rate = pd.read_csv(os.getenv("FILE_PATH_EXCHANGE_RATE_PROCESSED"))
    df_gdp = pd.read_csv(os.getenv("FILE_PATH_GDP_PROCESSED"))

    # Standardize the value column name across all tables
    # so they can be combined in long format
    df_ipca = df_ipca.rename(columns={'inflation_rate': 'value'})
    df_selic = df_selic.rename(columns={'selic_rate': 'value'})
    df_unemployment = df_unemployment.rename(columns={'unemployment_rate': 'value'})
    df_igpm = df_igpm.rename(columns={'igpm_rate': 'value'})
    df_exchange_rate = df_exchange_rate.rename(columns={'exchange_rate': 'value'})
    df_gdp = df_gdp.rename(columns={'gdp': 'value'})

    # Stack all tables vertically into a single long-format table
    df_unified = pd.concat([df_ipca, df_selic, df_unemployment, df_igpm, df_exchange_rate, df_gdp], ignore_index=True)

    # Save the final unified table (Gold layer)
    df_unified.to_csv(os.getenv("FILE_PATH_UNIFIED_TABLE"), index=False)

    print(df_unified.head(5))


# Run the full transformation pipeline

if __name__ == "__main__":

    transform_ipca()
    validate(pd.read_csv(os.getenv("FILE_PATH_IPCA_PROCESSED")), "IPCA")  # Validate after transformation

    transform_selic()
    validate(pd.read_csv(os.getenv("FILE_PATH_SELIC_PROCESSED")), "Selic")  # Validate after transformation

    transform_unemployment()
    validate(pd.read_csv(os.getenv("FILE_PATH_UNEMPLOYMENT_PROCESSED")), "Unemployment")  # Validate after transformation

    transform_igpm()
    validate(pd.read_csv(os.getenv("FILE_PATH_IGPM_PROCESSED")), "IGPM")  # Validate after transformation

    transform_exchange_rate()
    validate(pd.read_csv(os.getenv("FILE_PATH_EXCHANGE_RATE_PROCESSED")), "Exchange Rate")  # Validate after transformation

    transform_gdp()
    validate(pd.read_csv(os.getenv("FILE_PATH_GDP_PROCESSED")), "GDP")  # Validate after transformation

    create_unified_table()
    

 