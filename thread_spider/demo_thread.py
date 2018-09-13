import  requests
from bs4 import BeautifulSoup
import threading
import datetime

url_areas = []

# def get_url_areas():
url_base = 'https://bj.fang.ke.com/loupan/'
response_first = requests.get(url_base)
if response_first.status_code == 200:
    html_first = response_first.text
    soup_first = BeautifulSoup(html_first,'lxml')
    areas_info = soup_first.select('body > div.filter-container > div.filter-by-area-container > ul > li')
    for area_info in areas_info:
        area_name = area_info.text
        url_area_info = area_info.attrs['data-district-spell']
        url_first = url_base + url_area_info + '/'
        print('area_name-----------------',area_name)
        print('url_area_info-----------------',url_area_info)
        print('url_first-----------------',url_first)
        url_areas.append(url_first)

min = int(len(url_areas) / 2)

def get_house_info1():
    for url in url_areas[0:min]:
        response_second = requests.get(url)
        if response_second.status_code == 200:
            html_second = response_second.text
            soup_second = BeautifulSoup(html_second, 'lxml')
            _total_count = soup_second.select('body > div.resblock-list-container.clearfix > div.resblock-have-find > span.value')
            total_count = _total_count[0].text if _total_count else ''
            if int(total_count) % 10 == 0:
                total_page = int(int(total_count) / 10 )
            else:
                total_page = int(int(total_count) / 10 + 1)
            print('total_page-----------------', total_page)
            for page in range(1,total_page + 1):
                url_second = url + 'pg' + str(page)
                print('url_second-----------------',url_second)
                response_third = requests.get(url_second)
                if response_third.status_code == 200:
                    html_third = response_third.text
                    soup_third = BeautifulSoup(html_third,'lxml')
                    _rooms = soup_third.select('body > div.resblock-list-container.clearfix > ul.resblock-list-wrapper > li')
                    print('++++++++++++++++++++++++++++++',len(_rooms))
                    print(_rooms)
                    for room in _rooms:
                        _room_name = room.select('div.resblock-desc-wrapper > div.resblock-name > a')
                        room_name = _room_name[0].text if _room_name else ''

                        _img_info = room.select('a > img.lj-lazy')
                        img_info = _img_info[0].attrs['data-original'] if _img_info else ''

                        print('room_name----------------------',room_name)
                        print('img_info----------------------',img_info)


def get_house_info2():
    for url in url_areas[min:len(url_areas)]:
        response_second = requests.get(url)
        if response_second.status_code == 200:
            html_second = response_second.text
            soup_second = BeautifulSoup(html_second, 'lxml')
            _total_count = soup_second.select('body > div.resblock-list-container.clearfix > div.resblock-have-find > span.value')
            total_count = _total_count[0].text if _total_count else ''
            if int(total_count) % 10 == 0:
                total_page = int(int(total_count) / 10 )
            else:
                total_page = int(int(total_count) / 10 + 1)
            print('total_page-----------------', total_page)
            for page in range(1,total_page + 1):
                url_second = url + 'pg' + str(page)
                print('url_second-----------------',url_second)
                response_third = requests.get(url_second)
                if response_third.status_code == 200:
                    html_third = response_third.text
                    soup_third = BeautifulSoup(html_third,'lxml')
                    _rooms = soup_third.select('body > div.resblock-list-container.clearfix > ul.resblock-list-wrapper > li')
                    print('++++++++++++++++++++++++++++++',len(_rooms))
                    print(_rooms)
                    for room in _rooms:
                        _room_name = room.select('div.resblock-desc-wrapper > div.resblock-name > a')
                        room_name = _room_name[0].text if _room_name else ''

                        _img_info = room.select('a > img.lj-lazy')
                        img_info = _img_info[0].attrs['data-original'] if _img_info else ''

                        print('room_name----------------------',room_name)
                        print('img_info----------------------',img_info)



if __name__ == '__main__':
    print('******************************', url_areas)
    start = datetime.datetime.now()

    threads = []
    t1 = threading.Thread(target=get_house_info1,)
    threads.append(t1)
    t2 = threading.Thread(target=get_house_info2,)
    threads.append(t2)

    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()


    end = datetime.datetime.now()
    print('耗时-----------------',(end - start).seconds)
