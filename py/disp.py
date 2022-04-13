import eel
from numpy import size
from main import GetYahooInfo

zoom = 2.0 # ブラウザの拡大率 (default = 1.0)

@eel.expose
def main():
    get_info = GetYahooInfo(3210, False)
    weather = str(get_info.Weather())
    warn = str(get_info.Warn())
    kafun = str(get_info.Kafun())
    # print([weather, warn, kafun])
    return [weather, warn, kafun]

@eel.expose
def return_zoom():
    return zoom

eel.init('web')
eel.start('./disp.html', size=(1000*zoom, 490*zoom))
