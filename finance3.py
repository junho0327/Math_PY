import requests

import xml.etree.ElementTree as ET

## 호출하려는 OpenAPI URL를 정의합니다.

url = "http://ecos.bok.or.kr/api/StatisticItemList//xml/kr/1/1/021Y125/"

## 정의된 OpenAPI URL을 호출합니다.

response = requests.get(url)

## http 요청이 성공했을때 API의 리턴값을 가져옵니다.

if response.status_code == 200:

    try:

        contents = response.text

        ecosRoot = ET.fromstring(contents)

        ## 호출결과에 오류가 있었는지 확인합니다.

        if ecosRoot[0].text[:4] in ("INFO", "ERRO"):

            print(ecosRoot[0].text + " : " + ecosRoot[1].text)

            ## 오류메세지를 확인하고 처리합니다.

        else:

            print(contents)

            ## 결과값을 활용하여 필요한 프로그램을 작성합니다.

    except Exception as e:

        print(str(e))

        ##예외가 발생했을때 처리합니다
