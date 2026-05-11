import os
import requests
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("COINGECKO_API_KEY")

base_url = "https://api.coingecko.com/api/v3"
headers = {"x-cg-demo-api-key": API_KEY}

def test_api():
    # 1. Requisição Simples (GET)
    try:
        ping = requests.get(f"{base_url}/ping", headers=headers)
        ping.raise_for_status() # Verifica se houve erro (4xx ou 5xx)
        print(f"Status Ping: {ping.json()}")

        # 2. Requisição com Parâmetros
        params = {
            'ids': 'bitcoin',
            'vs_currencies': 'usd',
            'include_market_cap': 'true'
        }
        response = requests.get(f"{base_url}/simple/price", params=params, headers=headers)
        response.raise_for_status()
        print(f"Preço Bitcoin: {response.json()}")
        
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")

if __name__ == "__main__":
    test_api()