import requests
import pandas as pd

def unemployment_to_csv():

     # Fetch data from IBGE API
     url = "https://servicodados.ibge.gov.br/api/v3/agregados/6381/periodos/201201-202606/variaveis/4099?localidades=N1[all]"
     response = requests.get(url)

     # Convert JSON
     data = response.json()

     # Unpack nested JSON
     records = []
     for item in data[0]['resultados'][0]['series'][0]['serie'].items():
      records.append({
        'period': item[0],
        'unemployment_rate': item[1]
     })

     # Transform into table
     df = pd.DataFrame(records)
     print("Unemployment Table:")
     print(df)
     print(df.info())

     # Save to CSV

     df.to_csv("data/raw/unemployment.csv", index=False)
     print("\nFile saved at data/raw/unemployment.csv")

if __name__ == "__main__":
    unemployment_to_csv()