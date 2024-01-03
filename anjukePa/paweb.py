import re
from time import sleep

import requests_html
from bs4 import BeautifulSoup


class PaWeb:
    def __init__(self):
        pass

    @staticmethod
    def open_web_page(url):
        se = requests_html.HTMLSession()
        return se.get(url)

    def llist(self, n):
        house = []
        soup1 = BeautifulSoup(self.open_web_page(f'https://shanghai.anjuke.com/sale/p{n}/').text)
        sleep(2)
        tongji_tag = soup1.find_all('div', class_='property')
        for tongji_tags in tongji_tag:
            sss = tongji_tags.text.split('\n')
            arr = []
            for ssss in sss:
                arr.append(ssss.strip())
            # 分割名字与格局
            attribute = re.search(r'(\d+ 室 \d+ 厅 \d+ 卫)', arr[0]).group(1)  # 房子格局
            fname = arr[0].strip(attribute)  # 房子名
            area = arr[1]  # 面积
            direction = arr[2]  # 方向
            floor_height = arr[3]  # 楼层高度
            construction_time = arr[5]  # 建造时间
            # 空格分割
            fname_arr = arr[6].strip().split(' ')
            arr_fname = []
            try:
                fname_arr.append(arr[8])
            except:
                pass
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
                prce = arr_fname[8].split(' ')
                price = prce[0]
                unitprice = prce[2]
            dictionary = {
                '名称': fname,
                '户型': attribute,
                '面积': area,
                '朝向': direction,
                '楼层高度': floor_height,
                '建造时间': construction_time,
                '小区名': community,
                '所在位置': wherehome,
                '小区品质': is_it_close_to_the_subway,
                '户主': homo,
                '中介': intermediary,
                '价格/万': price,
                '单位价格': unitprice}
            house.append(dictionary)
        return house
