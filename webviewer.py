from bs4 import BeautifulSoup
from urllib.request  import urlopen
inputer = input("enter site(www.site.com):")
url = 'http://' + inputer
page = urlopen(url)
a = BeautifulSoup(page)
print(a.prettify())