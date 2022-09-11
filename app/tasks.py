import requests
import time
import json

def get_news_headlines(stock_input):
    headers = {
        'authority': 'api.nasdaq.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.6',
        'origin': 'https://www.nasdaq.com',
        'referer': 'https://www.nasdaq.com/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    }

    params = (
        ('q', f'{stock_input}|stocks'),
        ('offset', '0'),
        ('limit', '100'),
        ('fallback', 'false'),
    )
    time.sleep(10)
    response = requests.get('https://api.nasdaq.com/api/news/topic/articlebysymbol', headers=headers, params=params)
    result = response.json()

    news_dictionary = {
        f"{stock_input}": {
        "key": f"{stock_input}",
        "value": {
            f"news": {  
                "news_title": [result["data"]["rows"][i]["title"] for i in range(20)],
                "timestamp" : [result["data"]["rows"][i]["ago"] for i in range(20)] 
            }
        }        
        }
    }
    
    print(json.dumps(news_dictionary))
    return news_dictionary
