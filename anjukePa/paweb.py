import requests_html
import responses
from bs4 import BeautifulSoup
import html5lib
from parsel import Selector
import re
from time import sleep


class paweb:
    def __init__(self):
        self.soup = BeautifulSoup()

    def open_web_page(self, url):
        se = requests_html.HTMLSession()
        return se.get(url)

    def llist(self, n):
        house = []
        soup1 = BeautifulSoup(self.open_web_page(f'https://shanghai.anjuke.com/sale/p{n}/').text)
        sleep(2)
        slist = soup1.select('#esfMain > section > section.list-main > section.list-left > section:nth-child(4)')
        tongji_tag = soup1.find_all('div', class_='property')
        for tongji_tags in tongji_tag:
            sss = tongji_tags.text.split('\n')
            arr = []
            for ssss in sss:
                arr.append(ssss.strip())
            # 分割名字与格局
            attribute = re.search("(\d+ 室 \d+ 厅 \d+ 卫)", arr[0]).group(1)  # 房子格局
            fname = arr[0].strip(attribute)  # 房子名
            area = arr[1]  # 面积
            direction = arr[2]  # 方向
            floor_height = arr[3]  # 楼层高度
            i_don_t_know_what_it_is = arr[4]  # 暂时不知道是什么
            construction_time = arr[5]  # 建造时间
            # 空格分割
            fname_arr = arr[6].strip().split(' ')
            arr_fname = []
            for fname_arrs in fname_arr:
                arr_fname.append(fname_arrs.strip())
            community = arr_fname[0]  # 小区名
            wherehome = arr_fname[1]  # 所在位置
            is_it_close_to_the_subway = arr_fname[2]  # 是否靠近地铁
            homo = arr_fname[4]  # 户主
            intermediary = arr_fname[7]  # 中介
            try:
                price = arr_fname[11]  # 价格
                unitprice = arr_fname[13]  # 单位价格
            except:
                price = 9999
                unitprice = 9999
            dictionary = {
                'fname': fname,
                'attribute': attribute,
                'area': area,
                'direction': direction,
                'floor_height': floor_height,
                'i_don_t_know_what_it_is': i_don_t_know_what_it_is,
                'construction_time': construction_time,
                'community': community,
                'wherehome': wherehome,
                'is_it_close_to_the_subway': is_it_close_to_the_subway,
                'homo': homo,
                'intermediary': intermediary,
                'price': price,
                'unitprice': unitprice}
            house.append(dictionary)
        return house