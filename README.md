# [Prática] Consumindo APIs Rest

---

## 1. Escolha da API: CoinGecko

* **Objetivo:** Fornece dados em tempo real sobre o mercado de criptomoedas, incluindo preços, volume, capitalização de mercado e dados históricos.
* **Documentação Swagger:** [CoinGecko API V3 Docs](https://www.coingecko.com/en/api/documentation)

---

## 2. Análise Arquitetural

### **Aspectos Principais**

* **Base URL:** `https://api.coingecko.com/api/v3/`
* **Autenticação:** O plano demo exige uma **API Key** gratuita que deve ser enviada via **Header**(`x-cg-demo-api-key`) ou via **Query Parameter**(`?x_cg_demo_api_key=...`).
* **Versão:** O versionamento é feito diretamente na **URL** (`/v3/`). Garantindo atualizações na estrutura que não quebrem integrações antigas.
* **HATEOAS:** A API segue um modelo REST tradicional, onde você precisa conhecer os endpoints previamente através da documentação, em vez de receber links de navegação dinâmica no corpo da resposta, ou seja, sem utilização do HATEOAS.
* **Tipo de Resposta:** Estritamente **JSON**.

### **Estrutura de Objeto - coin_data**

```json
{
  "id": "bitcoin",
  "symbol": "btc",
  "name": "Bitcoin",
  "current_price": 65000.50,
  "last_updated": "2024-05-11T16:00:00.000Z"
}

```

---

## 3. Principais EndPoints

| Endpoint | Método | Descrição |
|----------|--------|-----------|
| `/ping` | `GET` | Verifica status operacional do servidor |
| `/global` | `GET` | Dados globais: número de moedas, market cap total e volume. |
| `/search/trending` | `GET` | Lista as moedas, NFTs e categorias que são tendência no momento |
| `/coins/markets` | `GET` | Tabela principal com preços, market cap e volume de moedas |
| `/coins/{id}` | `GET` | Dados completos de uma moeda |

## 4. Demonstração Rápida
`curl -X GET "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=brl" -H "x-cg-demo-api-key: API-KEY"`
