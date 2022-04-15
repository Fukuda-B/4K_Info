# 4K_Info
 Let's digital signage get started

### usage
```shell
git clone https://github.com/Fukuda-B/4K_Info
cd 4K_Info/py
python disp.py
```

### memo
|  |  |
| --- | --- |
| [./py/](./py/) | yahoo weather scraping |
| [./node/](./node/) | nothing |

### example

![./img0.jpg](./img0.jpg)

GetYahooInfo.Weather
```js
{
    0: {
        'date': '4月15日(金)',
        'weather': '曇時々雨',
        'temp_high': '11℃[-4]',
        'temp_low': '7℃[-1]',
        'fall': {
            '0-6': '---',
            '6-12': '---',
            '12-18': '---',
            '18-24': '60％'
        },
        'wind': '北の風後北東の風海上では北東の風やや強く',
        'wave': '1.5メートル'
    },
    1: {
        'date': '4月16日(土)',
        'weather': '晴一時雨',
        'temp_high': '14℃[+3]',
        'temp_low': '5℃[-2]',
        'fall': {
            '0-6': '60％',
            '6-12': '10％',
            '12-18': '0％',
            '18-24': '0％'
        },
        'wind': '北の風後北西の風海上では北東の風やや強く',
        'wave': '1.5メートル後1メートル'
    }
}
```

GetYahooInfo.Warn
```js
{
    0: {
        '注意報': 'なだれ、霜'
    }
}
```

GetYahooInfo.Kafun
```js
{
    0: {
        'date': '4/15(金)',
        'info': '少ない'
    },
    1: {
        'date': '4/16(土)',
        'info': '少ない'
    }
}
```
