
from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import datetime
date = datetime.today().strftime('%Y-%m-%d')

response = urlopen('https://finance.naver.com/sise/lastsearch2.nhn')
soup = BeautifulSoup(response, 'html.parser')

texttitle = str(date) + ".txt"
f = open(texttitle, 'w')
i = 1
for anchor in soup.select('td a'):
    f.write(str(i) + "위: " + anchor.get_text() + "\n")
    i = i + 1
f.close()