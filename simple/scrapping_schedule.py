import schedule
import time
import requests
import json

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
page = requests.get(url)
data = page.json()

def fetch_bitcoin():
    print("Getting Bitcoin Price ...")
    result = data['bpi']['USD']
    print(result)
    
def fetch_bitcoin_by_currency(x):
    print("Getting Bitcoin Price in ...", x)
    result = data['bpi'][x]
    print(result)
# creating time schedule example

schedule.every(10).seconds.do(fetch_bitcoin)
schedule.every(15).seconds.do(fetch_bitcoin_by_currency, 'GBP')
schedule.every(20).seconds.do(fetch_bitcoin_by_currency, 'EUR')

while True:
    schedule.run_pending()
    time.sleep(1)