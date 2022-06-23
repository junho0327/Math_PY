import requests

url = ' https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=&searchdate=20180102&data=AP01'
req = requests.get(url)
req

json_data = req.json()
json_data

import pandas as pd

data_frame = pd.DataFrame (json_data)
data_frame
