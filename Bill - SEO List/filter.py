from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from splinter import Browser
import os


# Created a function to generate a keyword list of custom size
def keyword_list(amount):
    keywords_df = pd.read_csv(r'Resources/Wordstream_petsupplies.csv')
    print("csv has been read.")

    keyword_list = []
    


    for x in range(amount):
        keyword_list.append(keywords_df['Keyword'][x])

    return keyword_list



def petsmart_scrape():
    url="https://www.petsmart.com/"
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    soup_meta = soup.find("meta", attrs={"name":"keywords"})
    keywords=soup_meta.get('content')
    keywords_list=keywords.split(",")
    del keywords_list[0]
    return keywords_list


def petland_scrape():
    url = 'http://petland.ca'
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    soup_meta = soup.find("meta", attrs={"name": "description"})
    keywords=soup_meta.get('content')
    keywords_list = keywords.split(',')
    return keywords_list



def scan(data_list, keyword_list):
    ratingcount = 0
    for word in data_list:
        for check in keyword_list:
            if (check in word):
                ratingcount = ratingcount + 1
                break
    return ratingcount



# A test call to the keyword and petsmart functions.

petsmart_list = petsmart_scrape()
petland_list = petland_scrape()

keyword_list_obj = keyword_list(400)


petland_hits = scan(petland_list, keyword_list_obj)
petsmart_hits = scan(petsmart_list, keyword_list_obj)


print(f"Petsmart hit {petsmart_hits} keyword results and Petland hit {petland_hits} keyword results")



print("Declaring dictionaries...")
petsmart_dict = {
        'URL':"https://www.petsmart.com/",
        'Keyword Tags':petsmart_list,
        'Keyword Hits':petsmart_hits,
}

petland_dict = {
        'URL':"http://petland.ca",
        'Keyword Tags':petland_list,
        'Keyword Hits':petland_hits,
}

keywords_dict = {
        "Petsmart Info":petsmart_dict,
        "Petland Info":petland_dict

}



print("Storing into PyMongo")

import pymongo
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.website_keywords
collection = db.petstores
db.petstores.delete_many({})

# figure out how to upload dictionary into the collection

print(keywords_dict)
collection.insert_one(keywords_dict)

#test
#results = db.petstores.find()
#for x in results:
#    print(x)

print("Testing pymongo insertion...")
results = db.petstores.find()
for x in results:
    print(x)