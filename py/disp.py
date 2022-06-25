import sys
import platform
import eel
from get_y_info import GetYahooInfo

zoom = 2.0          # ブラウザの拡大率 (default = 1.0)
area_id = 3210      # 地域
update = 5*60*1000 # 更新間隔 (ms)

@eel.expose
def main():
    get_info = GetYahooInfo(area_id, False)
    weather = str(get_info.weather())
    warn = str(get_info.warn())
    # kafun = str(get_info.kafun())
    # print([weather, warn, kafun])
    # return [weather, warn, kafun]

    weather_week = str(get_info.weather_week())
    return [weather, warn, weather_week]


@eel.expose
def return_zoom():
    return zoom

@eel.expose
def return_update():
    return update

eel.init('web')
if sys.platform in ['win32', 'win64'] and int(platform.release()) >= 10:
    eel.start('disp.html', mode='edge', size=(1000*zoom, 490*zoom))
else:
    eel.start('disp.html', size=(1000*zoom, 490*zoom))
