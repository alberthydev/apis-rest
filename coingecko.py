import os
import requests
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# Obtém a chave da variável de ambiente
API_KEY = os.getenv("COINGECKO_API_KEY")

base_url = "https://api.coingecko.com/api/v3"
headers = {"x-cg-demo-api-key": API_KEY}

def test_api():
    try:
        # 1. Requisição Global (Dados do Mercado)
        global_data = requests.get(f"{base_url}/global", headers=headers)
        global_data.raise_for_status()
        
        # O retorno do /global vem aninhado em uma chave "data"
        data = global_data.json().get("data", {})
        print("--- Dados Globais do Mercado ---")
        print(f"Moedas Ativas: {data.get('active_cryptocurrencies')}")
        print(f"Mercados (Exchanges): {data.get('markets')}")
        print(f"Dominância do BTC: {data.get('market_cap_percentage', {}).get('btc'):.2f}%")
        print("-" * 30)

        # 2. Requisição com Parâmetros (Preço Atual)
        params = {
            'ids': 'bitcoin',
            'vs_currencies': 'brl',
            'include_market_cap': 'true'
        }
        response = requests.get(f"{base_url}/simple/price", params=params, headers=headers)
        response.raise_for_status()
        
        print(f"Preço Bitcoin (USD): {response.json()}")
        
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")

if __name__ == "__main__":
    test_api()