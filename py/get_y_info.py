import datetime
import requests
from bs4 import BeautifulSoup

class GetYahooInfo():
    def __init__(self, area_id, parse):
        self.host = 'https://weather.yahoo.co.jp/weather/jp/5/'
        self.area = str(area_id)    # 地域
        self.parse = parse          # jsonパースするか
        self.minInt = 10            # 最小リクエスト間隔 (s)

    def _update(self):
        if not hasattr(self, 'rsLastUpdate') or self.soupLastUpdate < datetime.timedelta(seconds=self.minInt):
            url = self.host + self.area + ".html"
            r = requests.get(url)
            soup = BeautifulSoup(r.text, 'html.parser')
            self.soup = soup
            self.soupLastUpdate = datetime.datetime.today();

    def weather(self):
        ''' 天気予報 '''
        self._update() # 情報の更新
        soup = self.soup
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
                    'fall': {            # 降水確率
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
                    'fall': {             # 降水確率
                        '0-6': rs[28],
                        '6-12': rs[29],
                        '12-18': rs[30],
                        '18-24': rs[31],
                    },
                    'wind': rs[33],
                    'wave': rs[35],
                }
            }

    def warn(self):
        ''' 各種警報 '''
        self._update() # 情報の更新
        soup = self.soup
        rs = soup.find(class_='warnAdv_main')

        if not self.parse: return rs # parse option == False
        rs = [i.strip() for i in rs.text.splitlines()]
        rs = [i for i in rs if i != ""]
        rs.pop(0)
        res = {}
        for i in range(len(rs)//2):
            res[i] = {rs[i*2]: rs[i*2+1]}
        return res

    def kafun(self):
        ''' 花粉情報 (4月頃のみ?) '''
        self._update() # 情報の更新
        soup = self.soup
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

    def weather_week(self):
        ''' 週間予報 (jsonパース未対応)'''
        self._update() # 情報の更新
        soup = self.soup
        rs = soup.find(class_='yjw_table')

        if not self.parse: return rs # parse option == False
        rs = [i.strip() for i in rs.text.splitlines()]
        rs = [i for i in rs if i != ""]
        print(rs)


if __name__ == "__main__":
    get_info = GetYahooInfo(3210, True) # 地域: 3210，jsonパースあり

    wea = get_info.weather()
    print(wea)

    warn = get_info.warn()
    print(warn)

    # kafun = get_info.kafun()
    # print(kafun)
