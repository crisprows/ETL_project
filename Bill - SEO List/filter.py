from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from splinter import Browser
import os


# Created a function to generate a keyword list of custom size
def keyword_list(amount):
    keywords_df = pd.read_csv(r'Resources/Wordstream_petstores.csv')
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



#def keyword_scan(dataset, keyword_list):
    #for every cell(word) in dataset
    ###ratingcount = 0

    ###for word in dataset
    #see if word is in keyword list
    ###if keyword_list.contains(word):
    ###    ratingcount = ratingcount + 1
    ###    break
    ###endif
        #if word is in keyword list:
        # add to ratings count for dataset and then break/pass
    #   #end if
    # 
    ###return ratingcount
    #after for loop, return keyword rating - 
    #which is, amount of times the word was in the keyword_list


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

keyword_list_obj = keyword_list(400)

print("Running scan with these items:")
print(scan(petsmart_list, keyword_list_obj))