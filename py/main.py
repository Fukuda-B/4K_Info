from turtle import Turtle
import requests
from bs4 import BeautifulSoup

class GetYahooInfo():
    def __init__(self, area_id, parse):
        self.host = 'https://weather.yahoo.co.jp/weather/jp/5/'
        self.area = str(area_id)
        self.parse = parse

    def Weather(self):
        url = self.host + self.area + ".html"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        rs = soup.find(class_='forecastCity')

        if not self.parse: return rs # parse option == False
        rs = [i.strip() for i in rs.text.splitlines()]
        rs = [i for i in rs if i != ""]
        return {
                0: { # 今日
                    'date': rs[0],
                    'weather': rs[1],    # 天気
                    'temp_high': rs[2],  # 最高気温
                    'temp_low': rs[3],   # 最低気温
                    'fall': {           # 降水確率
                        '0-6': rs[10],
                        '6-12': rs[11],
                        '12-18': rs[12],
                        '18-24': rs[13],
                    },
                    'wind': rs[15],
                    'wave': rs[17],
                },
                1: { # 明日
                    'date': rs[18],
                    'weather': rs[19],    # 天気
                    'temp_high': rs[20],  # 最高気温
                    'temp_low': rs[21],   # 最低気温
                    'fall': {           # 降水確率
                        '0-6': rs[28],
                        '6-12': rs[29],
                        '12-18': rs[30],
                        '18-24': rs[31],
                    },
                    'wind': rs[33],
                    'wave': rs[35],
                }
            }

    def Warn(self):
        url = self.host + self.area + ".html"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        rs = soup.find(class_='warnAdv_main')

        if not self.parse: return rs # parse option == False
        rs = [i.strip() for i in rs.text.splitlines()]
        rs = [i for i in rs if i != ""]
        rs.pop(0)
        res = {}
        for i in range(len(rs)//2):
            res[i] = {rs[i*2]: rs[i*2+1]}
        return res

    def Kafun(self):
        url = self.host + self.area + ".html"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        rs = soup.find(class_='forecast')

        if not self.parse: return rs # parse option == False
        rs = [i.strip() for i in rs.text.splitlines()]
        rs = [i for i in rs if i != ""]
        return {
            0: {
                'date': rs[0],
                'info': rs[1],
            },
            1: {
                'date': rs[2],
                'info': rs[3],
            }
    }


if __name__ == "__main__":
    get_info = GetYahooInfo(3210, True)

    wea = get_info.Weather()
    print(wea)

    warn = get_info.Warn()
    print(warn)

    kafun = get_info.Kafun()
    print(kafun)
