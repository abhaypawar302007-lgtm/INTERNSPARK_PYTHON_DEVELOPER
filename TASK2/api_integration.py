import requests

def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1,
        "sparkline": False
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error fetching data:", response.status_code)
        return []

def display_data(data):
    print("\nTop 10 Cryptocurrencies:")
    for coin in data:
        print(f"{coin['name']} ({coin['symbol'].upper()}) | Price: ${coin['current_price']} | Market Cap: ${coin['market_cap']}")

def search_data(data, keyword):
    print(f"\nSearch results for '{keyword}':")
    for coin in data:
        if keyword.lower() in coin['name'].lower() or keyword.lower() in coin['symbol'].lower():
            print(f"Matched: {coin['name']} | Price: ${coin['current_price']}")

            
if __name__ == "__main__":
    crypto_data = fetch_crypto_data()
    display_data(crypto_data)

    keyword = input("\nEnter keyword to filter coins: ")
    search_data(crypto_data, keyword)
