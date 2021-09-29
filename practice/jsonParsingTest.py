import requests
import json
from urllib.request import urlopen
from urllib.parse import urlencode, quote_plus

API_KEY = ""

url = "https://at.agromarket.kr/openApi/price/sale.do"

queryParams = '?' + urlencode({
    quote_plus('serviceKey') : API_KEY,
    quote_plus('apiType') : 'json',
    quote_plus('pageNo') : '1',
    quote_plus('saleDate') : '20210622',
    quote_plus('whsalCd') : '110001',
    quote_plus('cmpCd') : '11000101'
})

response = requests.get(url + queryParams)
json_obj = response.json()


for data in json_obj['data']:
    print(f"KEY : 'midName' Value : {data['midName']} ")
