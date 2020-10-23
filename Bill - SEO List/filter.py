from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from splinter import Browser
import os


# Created a function to generate a keyword list of custom size from a specified source
def keyword_list(amount):
    keywords_df = pd.read_csv(r'Resources/Wordstream_petsupplies.csv')
    print("csv has been read.")

    keyword_list = []
    


    for x in range(amount):
        keyword_list.append(keywords_df['Keyword'][x])

    return keyword_list


# Michal's code for keyword scraping
def petsmart_scrape():
    url="https://www.petsmart.com/"
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    soup_meta = soup.find("meta", attrs={"name":"keywords"})
    keywords=soup_meta.get('content')
    keywords_list=keywords.split(",")
    del keywords_list[0]
    return keywords_list

# Christy's code for keyword scraping
def petland_scrape():
    url = 'http://petland.ca'
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    soup_meta = soup.find("meta", attrs={"name": "description"})
    keywords=soup_meta.get('content')
    keywords_list = keywords.split(',')
    return keywords_list



# Created a function to compare a list of keywords to a different list of targeted keywords
def scan(data_list, keyword_list):
    ratingcount = 0
    for word in data_list:
        for check in keyword_list:
            if (check in word):
                ratingcount = ratingcount + 1
                break
    return ratingcount



# Identify both lists as well as the keyword rating scores of both datasets as variables

petsmart_list = petsmart_scrape()
petland_list = petland_scrape()

keyword_list_obj = keyword_list(400)

petland_hits = scan(petland_list, keyword_list_obj)
petsmart_hits = scan(petsmart_list, keyword_list_obj)

# Shows results before declaring dictionary entries
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

# Having created a dictionary for each website, they're combined in a 
# dictionary of dictionaries to unify them and store them together.
keywords_dict = {
        "Petsmart Info":petsmart_dict,
        "Petland Info":petland_dict

}



# Michal's MongoDB framework, adjusted to "dictionary of dictionaries" format
print("Storing into PyMongo")

import pymongo
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.website_keywords
collection = db.petstores
db.petstores.delete_many({})

# insert_one inserts the dictionary object into MongoDB
collection.insert_one(keywords_dict)


# Test load insertion by printing collection results
print("Testing pymongo insertion...")
results = db.petstores.find()
for x in results:
    print(x)