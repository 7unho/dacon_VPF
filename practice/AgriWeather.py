import requests, bs4
import pandas as pd
from lxml import html
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote

# API_KEY = ""
API_KEY = ""

url = 'http://apis.data.go.kr/1390802/AgriWeather/WeatherObsrInfo/GnrlWeather/getWeatherYearMonList'

queryParams = '?' + urlencode({
    quote_plus('serviceKey') : API_KEY,
    quote_plus('Page_No') : '1',
    quote_plus('Page_Size') : '20',
    quote_plus('search_Year') : '2018',
    quote_plus('obsr_Spot_Code') : '210852A001'
})

response = urlopen(url + queryParams).read().decode('utf-8')
xmlObj = bs4.BeautifulSoup(response, 'lxml-xml')

rows = xmlObj.findAll('item')
columns = rows[0].find_all()

rowList = []
nameList = []
colList = []

rowsLen = len(rows)
for i in range(rowsLen):
    columns = rows[i].find_all()

    colLen = len(columns)
    for j in range(colLen):
        if i == 0:
            nameList.append(columns[j].name)
        eachColumn = columns[j].text
        colList.append(eachColumn)
    rowList.append(colList)
    colList = []

result = pd.DataFrame(rowList, columns=nameList)
result.head()
