#Current value of a Bitcoin in USD using the bitcoincharts api

import requests
import json

def get_bitcoin_price():
    url = 'http://api.bitcoincharts.com/v1/weighted_prices.json'
    response = requests.get(url)
    data = json.loads(response.text)
    return data['USD']['24h']

if __name__ == '__main__':
    print(get_bitcoin_price())
