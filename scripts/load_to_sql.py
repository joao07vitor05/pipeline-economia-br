import dotenv
import os
import pandas as pd
from sqlalchemy import create_engine
import time

dotenv.load_dotenv(encoding="utf-8")

csv_path = os.getenv("FILE_PATH_UNIFIED_TABLE")  # Connects to the CSV file


POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")


def load_to_sql():
    df = pd.read_csv(csv_path)  # Reads the CSV file into a DataFrame

    print(f"HOST={POSTGRES_HOST}")
    print(f"PORT={POSTGRES_PORT}")
    print(f"DB={POSTGRES_DB}")
    print(f"USER='{POSTGRES_USER}'")
    print(f"PASSWORD='{POSTGRES_PASSWORD}'")  

    engine = create_engine(
        f"postgresql+psycopg://"
        f"{POSTGRES_USER}:{POSTGRES_PASSWORD}"
        f"@{POSTGRES_HOST}:{POSTGRES_PORT}"
        f"/{POSTGRES_DB}"  

    )

    max_retries = 3  # Maximum number of connection attempts
    for attempt in range(1, max_retries + 1):
        try:
            # Send the DataFrame to a SQL table
            # if_exists="replace" drops and recreates the table each time
            df.to_sql("economic_indicators", engine, if_exists="append", index=False)
            print("Data successfully loaded into PostgreSQL!")
            break  # Exit loop on success
        except Exception as e:
            print(f"Attempt {attempt} failed: {e}")
            if attempt < max_retries:
                print("Connection failed, retrying in 5 seconds...")
                time.sleep(5)  # Wait before retrying
            else:
                raise  # Raise error after all retries are exhausted


if __name__ == "__main__":
    load_to_sql()