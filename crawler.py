import bs4
import urllib.request as url

page = url.urlopen ("https://www.youtube.com/")
webpage=bs4.BeautifulSoup(page)
data=webpage.find('div' , class_='item-details')
print(data.text)