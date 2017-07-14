import requests, json
from bs4 import BeautifulSoup

# 롯데시네마 api parameter
# paramList={"MethodName":"GetPlaySequence","channelType":"HO","osType":"Chrome","osVersion":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36","playDate":"2017-07-14","cinemaID":"1|3|4002","representationMovieCode":""}
# 1|3|4002, 1|3|4006 -> cinemaID 백화점, 둔산
# json 반환

# megabox
# https://www.megabox.co.kr/pages/timetable/TimeTable_Cinema_List.jsp
# Accept: text/html, */*; q=0.01
# Accept-Encoding: gzip, deflate
# Content-Type: application/x-www-form-urlencoded
# cinemaCode=3021&playDate=2017-07-14
#
#

# cgv page parsing
cgvtheaters = ['0007', '0154', '0202', '0127', '0206', '0209']  # 대전, 가오, 탄방, 터미널, 노은, 유성온천
lottetheaters = ['1|3|4002', '1|3|4006']
megatheaters = ['3021']
cormovie = {};


def spider(date, name):
    # cgv request and parsing
    # for theater in cgvtheaters:
    #     url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=03,205&theatercode=' + str(
    #         theater) + '&date=' + str(date)
    #     source_code = requests.get(url)
    #     plain_text = source_code.text
    #     soup = BeautifulSoup(plain_text, 'lxml')
    #     moviedivs = soup.select("div > div > ul > li > div")
    #     for moviediv in moviedivs:
    #         if moviediv.select("div > a > strong").__len__() == 0:
    #             pass
    #             continue
    #         if moviediv.select("div > a > strong")[0].string.strip().find(name) != -1:
    #             cormovie.__setitem__(theater, moviediv)
    #

    for theater in lottetheaters:
        url = "http://www.lottecinema.co.kr/LCWS/Ticketing/TicketingData.aspx"
        headers = {'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
        data = 'paramList={"MethodName": "GetPlaySequence", "channelType": "HO", "osType": "Chrome","osVersion": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36","playDate": "'+date[0:4]+'-'+date[4:6]+'-'+date[6:8]+'", "cinemaID": "'+str(theater)+'", "representationMovieCode": ""}'

        json_data = requests.post(url, headers = headers, data=data)



spider("20170714", "스파이더맨")
