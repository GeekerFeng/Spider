import requests
from bs4 import BeautifulSoup
import time
import re
import random
import sys

class Get_ip():
    def __init__(self):
        self.url=['http://www.xicidaili.com/nn/','http://www.xicidaili.com/nt/']
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive'}
    def run(self,type=0):
        html=requests.get(self.url[type],headers=self.headers).text
        table=BeautifulSoup(html,"html.parser").find("table").find_all("tr")
        
        port=[]
        info={'ip':'','port':'','addr':'','anonymous':'','type':'','speed':'','conn_time':'','alive_time':'','test_time':''}
        for item in table[1:]:
            lists =item.find_all('td')
            info['ip']=lists[1].get_text()
            info['port']=lists[2].get_text()
            info['addr']=lists[3].get_text().replace('\n', '')
            info['anonymous']=lists[4].get_text()
            info['type']=lists[5].get_text()
            info['speed']=lists[6].div['title']
            info['conn_time']=lists[7].div['title']
            info['alive_time']=lists[8].get_text()
            info['test_time']=lists[9].get_text()
            port.append(info)
        return port
            


if __name__=='__main__':
    ip=Get_ip()
    print (ip.run(int(sys.argv[1])))