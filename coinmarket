from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import ssl


context = ssl._create_unverified_context()

# assigning the url to my_url varriable
my_url = "https://coinmarketcap.com"

# opening up connection, grabbing the page
uClient = uReq(my_url, context=context)
# offload the content to variable python
page_html = uClient.read()

uClient.close()
# html parsing
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("tr", {"class":"odd"})
