import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 
import datetime

my_url = 'https://www.sgmaritime.com/company-listings'

# opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parser
page_soup = soup(page_html, 'html.parser')

# find desired item
url_link = page_soup.findAll("div",{"class":"col-md-9 col-xs-8 company-details"})

# filename = "company_prof.csv"
# f = open(filename, "w")
# headers =  "company_name, company_address, company_description, company_email, company_phone, company_fax, company_web, company_map, company_product, company_categories "
# f.write(headers)

for i in url_link:
    #get url name
    url_name = 'https://www.sgmaritime.com' + i.h3.a['href']
    uClient = uReq(url_name)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, 'html.parser')
    # print(url_name)
    
    # get company name
    company_name = page_soup.findAll("div",{"class":"col-md-9 company-details"})[0].h3.text
    print(company_name)

    #get company address
    company_address = page_soup.findAll("div",{"class":"col-md-7 company-contact"})[0].p.text.strip()
    print(company_address)
    
    #get company description
    company_description = page_soup.findAll("div",{"class":"company-description"})[0].text 
    print(company_description)

    #get company email
    company_email = page_soup.findAll("font",{"id":"companyEmail"})
    if company_email == [] :
        print("None")
    else:
        print(company_email[0]["onclick"][17:40].split(",")[0])

    #get company phone 
    company_phone = page_soup.findAll("div",{"class":"valuephone"})[0].a["href"].strip()
    print(company_phone)

    #get company fax 
    company_fax = page_soup.findAll("div",{"class":"valuefax"})
    if company_fax == [] :
        print("None")
    else:
        print(company_fax[0].a["href"].strip())

    #get company web address
    company_web = page_soup.findAll("div",{"id":"valuewebsite"})
    if company_web == [] :
        print("None")
    else:
        print(company_web[0].a["href"].strip())

    #get company map
    company_map = page_soup.findAll("div",{"class":"col-md-5 company-map"})[0].iframe['src']
    print(company_map)

    #get company product and services
    company_product = page_soup.findAll("div",{"class":"item"})
    if company_product == [] :
        print("None")
    else:
        print('https://www.sgmaritime.com' + company_product[0].a["href"].strip())

    #get company categories
    company_categories = page_soup.findAll("div",{"class":"company-description"})
    if company_categories == [] :
        print("None")
    else:
        print('https://www.sgmaritime.com' + company_categories[1].ul.ul.li.a["href"])
    
    print('\n')
    
    #f.write("\n" + company_name + "," + company_address + "," + company_description + "," + company_email[0]["onclick"][17:40].split(",")[0] + "," +  company_phone + "," + company_fax[0].a["href"].strip() + "," + company_web[0].a["href"].strip() + "," + company_map + "," + 'https://www.sgmaritime.com' + company_product[0].a["href"].strip() + "," + 'https://www.sgmaritime.com' + company_categories[1].ul.ul.li.a["href"] +"\n" )

# f.close()


    





