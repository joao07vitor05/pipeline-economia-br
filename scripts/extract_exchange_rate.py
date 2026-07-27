import requests 
import pandas as pd

def exchange_rate_to_csv():

    # Fetch data from Central Bank API
    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados?dataInicial=01/01/2020&dataFinal=30/06/2026&formato=json"
    response = requests.get(url)

     # Convert JSON to Python list
    data = response.json()
    print("Raw data:", data)

     # Transform into table
    df = pd.DataFrame(data)
    print("\nTable:")
    print(df.head())
    print(df.info())

     # Save to CSV
    df.to_csv("data/raw/exchange_rate.csv", index=False)
    print("\nFile saved at data/raw/exchange_rate.csv")

if __name__ == "__main__":
    exchange_rate_to_csv()