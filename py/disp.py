import eel
from numpy import size
from main import GetYahooInfo

@eel.expose
def main():
    get_info = GetYahooInfo(3210, False)
    weather = str(get_info.Weather())
    warn = str(get_info.Warn())
    kafun = str(get_info.Kafun())
    # print([weather, warn, kafun])
    return [weather, warn, kafun]

eel.init('web')
eel.start('./disp.html', size=(1000, 600))
