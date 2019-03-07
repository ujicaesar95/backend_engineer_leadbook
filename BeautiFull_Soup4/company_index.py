import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 
import datetime

my_url = "https://www.sgmaritime.com/company-listings"

# opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parser
page_soup = soup(page_html, "html.parser")

# find desired item
company_listing = page_soup.findAll("div",{"class":"company-listing"})
url_link = page_soup.findAll("div",{"class":"col-md-9 col-xs-8 company-details"})

filename = "company_index.csv"
f = open(filename, "w")
headers =  "company_name, url_name, crawled_on"
f.write(headers)

for i in company_listing:
    
    # get company name
    company_name = i.div.a.img['alt']
    print(company_name)

    #get url name
    url_name = i.h3.a['href']
    print('url = ' + 'https://www.sgmaritime.com' + url_name)
    
    #get datetime when web being be crawled
    datelist = []
    crawled_on = datetime.date.today()
    datelist.append(crawled_on)
    print(str(crawled_on))

    f.write("\n" + company_name + "," + 'https://www.sgmaritime.com' + url_name + "," + str(crawled_on) + "\n" )

f.close()
    





