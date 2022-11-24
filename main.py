from bs4 import BeautifulSoup
import urllib.request
import urllib.error
import re

html_page = urllib.request.urlopen("https://ru.wikipedia.org/wiki/%D0%93%D0%B8%D0%BF%D0%B5%D1%80%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B0")
soup = BeautifulSoup(html_page, 'html.parser')
for link in soup.find_all('a' , attrs= {'href': re.compile('^https://')}):
    print (link.get('href'))

