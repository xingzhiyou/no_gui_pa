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
        house = []
        soup1 = BeautifulSoup(self.open_web(f'https://sh.zu.anjuke.com/fangyuan/p{n}/').text)
        connect = soup1.find_all('div', class_='zu-itemmod clearfix')
        for connects in connect:
            name = connects.find_all('b', class_='strongbox')
            name = name[0].text
            b_tag = connects.find_all('p', class_='details-item tag')
            b_tag = b_tag[0].text

            dictionary = {
                '名字': name,
            }
            house.append(dictionary)
        print(house)


PaWeb().llist(1)
