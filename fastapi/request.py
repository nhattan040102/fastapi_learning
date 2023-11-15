import requests
import random
from datetime import datetime

symbol_list = ["BTC", "LTX", "APL"]

url = "http://localhost:8000/trading_data"
data = {
    "id": int(datetime.now().timestamp()),
    "symbol": symbol_list[random.randint(0, 2)],
    "amount": round(random.uniform(0,4), 2)
}

query_params = {
    "symbol": "AAPL"
}

response = requests.post(url, json=data)


print(response.status_code)
print(response.json())