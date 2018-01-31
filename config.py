#!/usr/bin/env python3

import json
import urllib.request


class CryptoCurrency:
    def __init__(self, x):
        url = urllib.request.urlopen("https://api.coinmarketcap.com/v1/ticker/?limit=10")
        json_ported = json.load(url)
        self.json_ported = json_ported
         # x is a number in json massive from API
        self.x = x

    def printing(self):
        print(self.json_ported[self.x]['name'])
        print(self.json_ported[self.x]['price_usd'])

    def crypto_value(self):
        naming = self.json_ported[self.x]['name']
        pricing = self.json_ported[self.x]['price_usd']
