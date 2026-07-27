import requests
import pandas as pd

def ipca_to_csv():
     
     # Fetch data from IBGE API
     url = "https://servicodados.ibge.gov.br/api/v3/agregados/1737/periodos/201501-202606/variaveis/63?localidades=N1[all]"
     response = requests.get(url)

     # Convert JSON
     data = response.json()

     # Unpack nested JSON
     records = []
     for item in data[0]['resultados'][0]['series'][0]['serie'].items():
         records.append({
        'period': item[0],
        'value': item[1]
    })

     # Transform into table
     df = pd.DataFrame(records)
     print("IPCA Table:")
     print(df)
     print(df.info())

     # Save to CSV
     df.to_csv("data/raw/ipca.csv", index=False)
     print("\nFile saved at data/raw/ipca.csv")

if __name__ == "__main__":
    ipca_to_csv() 