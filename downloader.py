# -*- coding: utf-8 -*-
"""
Spyder Editor

Author: RAM
Affiliation: NCAT
Date: 02/13
"""
import requests
from bs4 import BeautifulSoup

"""
Parameeters
"""
ransomsearch = "Razi"
pages_to_crawl = 5
download_active = 0

"""
Defined
"""
result_per_page = 20
dlink2 = []

"""
Crawler code
"""
with requests.Session() as s:
    url = "https://virusshare.com/processlogin"
    url2 = "https://virusshare.com/search"
    s.get(url)
    payload = {
        "username":"rawshan",
        "password":"S3dE5E5ED4E1"
        }
    res = s.post(url, data=payload)
    print(res.url, "\n") 
    
    payload2 = []
    for i in range(0,pages_to_crawl):
        payload2.append({"search":ransomsearch,"skip":str(i*result_per_page)})
        print("parsing page",str(i))
        #print(payload2[i])
        res2 = s.post(url2, data=payload2[i])
        #print(res2.content)
        html_page = res2.text
        soup = BeautifulSoup(html_page, "html.parser")
        for link in soup.findAll('a'):
            dlink = link.get('href')
            if str(dlink).startswith("download?"):
                dlink2.append("https://virusshare.com/"+str(dlink))
    

    print("\n*",ransomsearch,"*","found, total =", len(dlink2))
    if download_active: 
        j=1 
        for i in dlink2:
            res3 = s.get(i)
            open(ransomsearch+str(j)+'.zip', 'wb').write(res3.content)
            j = j+1   
        print("Download completed")
    
    print("END")