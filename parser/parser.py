import requests
from bs4 import BeautifulSoup

url = "https://uaserials.pro/films/page/"
for i in range(1,10):
    url_new = url
    url_new+= str(i)
    url_new+= "/"
    r = requests.get(url_new)
    soup = BeautifulSoup(r.text, features="html.parser")
    soup_list_name = soup.find_all('div',{'class':'th-title truncate'})


    for i in soup_list_name:
        print(i.text)