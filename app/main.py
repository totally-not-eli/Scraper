# from sources import *

from scipy import stats
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests

from re import sub


item_name = []
prices = []

for i in range(1,10):

    ebayUrl = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=iphone+13+pro+max&_sacat=0&LH_TitleDesc=0&_pgn="+str(i)

    r = requests.get(ebayUrl)

    data = r.text
    soup = BeautifulSoup(data,features="html.parser")
    listings = soup.find_all('li', attrs={'class': 's-item'})

    print(listings)

    for listing in listings:
        prod_name = " "
        prod_price = " "
        for name in listing.find_all(attrs={'class':"s-item__detail"}):
            if(str(name.find(text=True, recursive=False))!="None"):
                prod_name=str(name.find(text=True, recursive=False))
                item_name.append(prod_name)

        if(prod_name != " "):
            price = listing.find(attrs={'class':"s-item__price"})
            prod_price = str(price.find(text=True, recursive=False))
            prod_price = int(sub(",","",prod_price.split("INR")[1].split(".")[0]))
            prices.append(prod_price)


data_note_8 = pd.DataFrame({"Name":item_name, "Prices": prices})

print(data_note_8)