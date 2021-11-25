#!/usr/bin/env python3
# encoding = utf-8
# Windows Only

import winsound, time, requests, re
from bs4 import BeautifulSoup

def Beep():
    interval = 200
    frequency = 2500
    count = 10
    for t in range(count):
        winsound.Beep(frequency, interval)
        time.sleep(interval / 1000)

def main():
    URL = "https://greencloudvps.com/billing/store/black-friday-2021"
    regex = r"product\d*-name"
    keyword = "JP"
    while True:
        response = requests.get(URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        itemList = soup.find_all(id=re.compile(regex))
        itemList = list(map(lambda item: item.get_text(), itemList))
        print(itemList)
        wantedItemList = list(filter(lambda item: item.find(keyword)!= -1, itemList))
        print(wantedItemList)
        if len(wantedItemList) != 0:
            Beep()
        time.sleep(20)
    
    
if __name__ == '__main__':
    main()
