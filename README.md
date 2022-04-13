# 4K_Info
 Let's digital signage get started

### usage
`py main.py`

### memo
|  |  |
| --- | --- |
| [./py/](./py/) | yahoo weather scraping |
| [./node/](./node/) | nothing |

### example
GetYahooInfo.Weather
```js
{
    0: {
        'date': '4月13日(水)',
        'weather': '曇一時雨',
        'temp_high': '16℃[-6]',
        'temp_low': '10℃[+1]',
        'fall': {
            '0-6': '---',
            '6-12': '---',
            '12-18': '---',
            '18-24': '50％'
        },
        'wind': '北の風海上では後北の風やや強く',
        'wave': '1メートル後1.5 メートル'
    },
    1: {
        'date': '4月14日(木)',
        'weather': '曇り',
        'temp_high': '16℃[0]',
        'temp_low': '7℃[-3]',
        'fall': {
            '0-6': '10％',
            '6-12': '10％',
            '12-18': '30％',
            '18-24': '30％'
        },
        'wind': '北の風後南東の風海上では北の風やや強く',
        'wave': '1.5メートル後1メートル'
    }
}
```

GetYahooInfo.Warn
```js
{
    0: {
        '注意報': '濃霧、なだれ'
    }
}
```

GetYahooInfo.Kafun
```js
{
    0: {
        'date': '4/13(水)',
        'info': '少ない'
    },
    1: {
        'date': '4/14(木)',
        'info': '非常に多い'
    }
}
```
