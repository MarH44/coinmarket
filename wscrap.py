
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import ssl
import time


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
#grab each product
containers = page_soup.findAll("tr")[1:]


#for container in containers:
 #       Name = container.img["alt"]



for container in containers:
    print("")
    icos_name = container.img["alt"]
    #icos_name = container.span.string
    #icos_name = container.span.text
    print(icos_name)

    icos_short_name = container.a.text
    print(icos_short_name)

    icos_price = container.find("a", attrs={"data-usd" : True}).getText()
    print(icos_price)

    precent_change = container.find("a", {"class":"no-wrap percent-change  Text-right Negative_change"})
    print(precent_change)

    
   
    



        
        
    





