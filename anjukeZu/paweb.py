import requests_html
from bs4 import BeautifulSoup


class PaWeb:
    def __init__(self):
        pass

    @staticmethod
    def open_web(url):
        se = requests_html.HTMLSession()
        return se.get(url)

    def llist(self, n):
        soup1 = BeautifulSoup(self.open_web(f'https://sh.zu.anjuke.com/fangyuan/p{n}/').text)
        # 获取总页数
        for title in soup1.select('div.list-content'):
            house = []
            # 获取每一页的房源信息
            for title_house in title.select('div.zu-itemmod'):
                # 获取房源名称
                house_name = title_house.select_one('b.strongbox').text
                # 获取房源标签
                house_tags = []
                for i in title_house.select('p b.strongbox'):
                    house_tags.append(i.text)
                # 获取房源户型
                house_type = house_tags[0] + '室' + house_tags[1] + '厅'
                # 获取房源信息
                p_tag = title_house.find('p')
                cid = list(p_tag.children)
                # 获取房源楼层
                if cid[-1].text.find('层') != -1:
                    house_tags.append(cid[-1].text)
                else:
                    house_tags.append(cid[-3].text)
                # 获取房源信息
                details = title_house.find('address')
                did = list(details.children)
                house_where = ''.join(did[1].text.strip())  # 小区
                house_area = ''.join(did[2].text.strip())  # 区
                house_town = ''.join(did[4].text.strip())  # 城镇
                house_price = ''.join(did[6].text.strip())  # 地址
                # 获取房源详情
                details = title_house.find_all('span', class_='cls-common')
                shared_rental = details[0].text  # 是否合租
                facing = details[1].text  # 朝向

                did = []

                if '有电梯' in details[-2].text and '线' in details[-1].text:  # 地铁
                    did.append(details[-1].text)
                    did.append(details[-2].text)

                elif details[-1].text.find('有电梯') != -1:  # 电梯
                    did.append('无地铁')
                    did.append(details[-1].text)

                else:
                    did.append('无地铁')
                    did.append('无电梯')

                price = title_house.find('strong', class_='price').text  # 价格
                # 将房源信息存入字典
                dictionary = {
                    '名称': house_name,
                    '户型': house_type,
                    '面积': house_tags[2],
                    '楼层': house_tags[-1],
                    '小区': house_where,
                    '区': house_area,
                    '城镇': house_town,
                    '地址': house_price,
                    '是否合租': shared_rental,
                    '朝向': facing,
                    '地铁': did[0],
                    '电梯': did[1],
                    '价格': price
                }
                house.append(dictionary)
            return house
