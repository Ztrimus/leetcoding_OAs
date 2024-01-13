import requests
import os

url = "https://jsonmock.hackerrank.com/api/countries/search?region={}&name={}"

def fetch_all_data(region, keyword, page=1):
        resultFirstHit = requests.get(url.format(region, keyword) + (f"&page={page}" if page>1 else '')).json()
    
        per_page = resultFirstHit['per_page']
        total_records = resultFirstHit['total']
        total_pages = resultFirstHit.get('total_pages', 0)
        data = resultFirstHit.get('data', [])
        
        result = {item['name']:item['population'] for item in data}
        if page < (total_records//per_page+1):
            result.update(fetch_all_data(region, keyword, page+1))
        return result

def findCountry(region, keyword):
    modified_data = fetch_all_data(region, keyword)
    sorted_data = sorted(modified_data.items(), key=lambda x: (x[1],x[0]))
    for key, value in sorted_data:
        print(f"{key}, {value}")

result = findCountry("Europe", "de")
result = findCountry("Asia", "ab")