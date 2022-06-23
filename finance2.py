from bs4 import BeautifulSoup
import urllib.request as urlReq
import datetime

url = 'https://finance.naver.com/marketindex/'
html = urlReq.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

# 날짜와 현재시간을 출력하기 위한 변수
exchange_date = datetime.date.today()
exchange_time = datetime.datetime.now()

# 각각 미국달러, 일본엔화, 유럽연합 유로, 중국 위안
# 각 국가에 해당하는 html 코드를 잘라놓는다.
usd = '#exchangeList > li > a.head.usd '
jpy = '#exchangeList > li > a.head.jpy '
eur = '#exchangeList > li > a.head.eur '
cny = '#exchangeList > li > a.head.cny '

# 각 국가별로 하나하나 선언하기엔 너무 길어저서 html코드상 공통부분을 잘라내놓는다.
price = '> div > span.value'
change = '> div > span.change'
blind = '> div > span.blind'


# 각 국가별 가격, 변동가격, 변동 출력함수. 파일정보와 국가를 변수로 받는다.
def fill_value(file, country):
    getprice = soup.select_one(country + price).string
    getchange = soup.select_one(country + change).string
    getblind = soup.select_one(country + blind).string
    file.write(f"\n가격 : {getprice}\n변동가격 : {getchange}\n변동 : {getblind}")
    file.write('\n\n')
    return


# 파일이름 선언
file_name = exchange_date.strftime('%Y%m%d') + '_' + exchange_time.strftime('%H%M%S') + '.txt'

# 파일 출력부분
with open(file_name, 'w', encoding='utf-8', newline='') as f:
    f.write(f"{exchange_date.strftime('%Y %m %d %A')} {exchange_time.strftime('%H:%M:%S')}")
    f.write('\n\n')
    f.write("미국 USD")
    fill_value(f, usd)
    f.write("유럽연합 EUR")
    fill_value(f, eur)
    f.write("일본 JPY")
    fill_value(f, jpy)
    f.write("중국 CNY")
    fill_value(f, cny)