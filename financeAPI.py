from urllib.request import urlopen
import json

url = "https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=&searchdate=20180102&data=AP01"
responseBody = urlopen(url + "1").read().decode('utf-8')
jsonArray = json.loads(responseBody)
storeInfosArray = jsonArray.get("storeInfos")
numPage = jsonArray.get("totalPages")
print(storeInfosArray)

for i in range(2, numPage + 1):
    responseBody = urlopen(url + str(i)).read().decode('utf-8')
    jsonArray = json.loads(responseBody)
    storeInfosArray = jsonArray.get("storeInfos")
    print(storeInfosArray)
