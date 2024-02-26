import json
import requests

NUMBER = 1000
PSID = {
    'A++': 27099781,  # 典範級
    'A+': 27099788,  # 甲級
    'A': 27099794,  # 優良級
    'B': 27099795,  # 乙級
    'C': 27099797,  # 丙級
    'D': 27099799,  # 初級
    'E': 27099802,  # 小作品級
    'N': 27099800  # 未評級
}


if __name__ == '__main__':
    TITLES = dict()
    S = requests.Session()
    URL = "https://petscan.wmflabs.org"
    for rating in PSID:
        print(rating)
        PARAMS = {
            "psid": PSID[rating],
            "format": "json",
            'doit': ""
        }
        R = S.get(url=URL, params=PARAMS)
        DATA = R.json()['*'][0]['a']['*']
        TITLE_LIST = list(map(lambda item: item['title'], DATA))
        TITLES[rating] = TITLE_LIST

    with open('titles.json', 'w', encoding='utf-8') as file:
        json.dump(TITLES, file, ensure_ascii=False, indent=4)
