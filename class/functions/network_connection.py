import asyncio
import http
import requests
import time

class Requesting:
    def __init__(self):
        self.website = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
        self.params = {"ids":"bitcoin","vs_currency":"usd","days":3}
        self.got_it = ""
    
    def get_it(self):
        a =requests.get(self.website, params=self.params)
        self.got_it = a.json()
        self.temp = self.got_it["prices"]
        self.list1 = []
        self.list2 = []
        for i in self.temp:
            
            self.list1.append(time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(i[0]/1000)))
            self.list2.append(i[1])
        
        return self.list1,self.list2
