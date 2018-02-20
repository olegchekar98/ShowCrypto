#!/usr/bin/env python3

import json
from settings import data


class CryptoCurrency:
    def __init__(self, x):
        self.json_ported =  json.load(data)
         # x is a number in json massive from API
        self.x = x
        self.naming = self.json_ported[self.x]['name']
        self.pricing = self.json_ported[self.x]['price_usd']

    def printing(self):
        print(self.json_ported[self.x]['name'])
        print(self.json_ported[self.x]['price_usd'])


