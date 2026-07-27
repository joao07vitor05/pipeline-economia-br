import dotenv
import pandas as pd
import os
from dotenv import load_dotenv

dotenv.load_dotenv()

def validate(df, name):

    """
    Run basic data quality checks on a DataFrame.

    df: the DataFrame to validate
    name: label used in error/success messages
    """


    assert not df.empty, f"{name}: DataFrame is empty!"   # Fail early if the dataset has no rows

    nulls = df.isnull().sum().sum()  # Fail if there are any missing (null) values
    assert nulls == 0, f"{name}: Contains {nulls} null values!"


    duplicates = df.duplicated().sum()    # Fail if there are any fully duplicated rows
    assert duplicates == 0, f"{name}: Contains {duplicates} duplicate rows!"
    
    print(f"✅ {name}: All validations passed!")

if __name__ == "__main__":
     validate(pd.read_csv(os.getenv("FILE_PATH_IPCA_PROCESSED")), "IPCA")
     validate(pd.read_csv(os.getenv("FILE_PATH_SELIC_PROCESSED")), "Selic")
     validate(pd.read_csv(os.getenv("FILE_PATH_UNEMPLOYMENT_PROCESSED")), "Unemployment")
     validate(pd.read_csv(os.getenv("FILE_PATH_IGPM_PROCESSED")), "IGPM")
     validate(pd.read_csv(os.getenv("FILE_PATH_EXCHANGE_RATE_PROCESSED")), "Exchange Rate")
     validate(pd.read_csv(os.getenv("FILE_PATH_GDP_PROCESSED")), "GDP")