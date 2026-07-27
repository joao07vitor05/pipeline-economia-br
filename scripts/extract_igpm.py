import requests
import pandas as pd

def igpm_to_csv():
        
        # Fetch data from Central Bank API
        url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.189/dados?dataInicial=01/01/2020&dataFinal=30/06/2026&formato=json"
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
        df.to_csv("data/raw/igpm.csv", index=False)
        print("\nFile saved at data/raw/igpm.csv")

if __name__ == "__main__":
        igpm_to_csv()