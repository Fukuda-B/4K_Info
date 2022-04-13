import sys
import platform
import eel
from main import GetYahooInfo

zoom = 1.5          # ブラウザの拡大率 (default = 1.0)
area_id = 3210      # 地域
update = 5*60*1000 # 更新間隔 (ms)

@eel.expose
def main():
    get_info = GetYahooInfo(area_id, False)
    weather = str(get_info.Weather())
    warn = str(get_info.Warn())
    kafun = str(get_info.Kafun())
    # print([weather, warn, kafun])
    return [weather, warn, kafun]

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
