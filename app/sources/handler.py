from sources.helper import Helper
import requests
from bs4 import BeautifulSoup
import pandas as pd


class Handler(Helper):
    def __init__(self):
        self.list_urls = []
        self.list_objects = []
    
    def get_all_name_price(self,
                        device,
                        number_of_pages, 
                        type_of_object):
    
        str_device = str(device).replace(" ","+")
        link = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=" + str_device + "&_sacat=0&LH_TitleDesc=0&_pgn="
        self.list_urls.append(link)
        self.list_objects.append(type_of_object)
        
        list_of_names = []
        list_of_prices = []

        # send a request
        # then get the name of the product
        # then get the price

        for _ in range(number_of_pages):
            ebay_url = link + str(_)
            req = requests.get(ebay_url)
            data = req.text
            soup = BeautifulSoup(data, 'html.parser')
            listings = soup.find_all("li", attrs = {'class' : "s-item"})

            if listings:
                for listing in listings:
                    prod_name = " " # for reference if we get no data
                    prod_price = " " # for reference
                    for name in listing.find_all(attrs = {'class' : "s-item__title"}):
                        prod_name = str(name.text.strip())
                        list_of_names.append(prod_name)

                    if prod_name != " ":
                        prod_price = listing.find(attrs = {'class': "s-item__price"})
                        list_of_prices.append(prod_price.text.strip())
        
        dictionary = {"item_name" : list_of_names,
                      "item_price" : list_of_prices}

        data_frame = pd.DataFrame(dictionary)

        print(data_frame)                     
        

        
            

