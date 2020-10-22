from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from splinter import Browser


# Created a function to generate a keyword list of custom size
def keyword_list(amount):
    keywords_csv = "Resources/Wordstream_pet_NJ.csv"
    keywords_df = pd.read_csv(r'Resources/Wordstream_pet_NJ.csv')
    print("csv has been read.")

    keyword_list = []
    


    for x in range(amount):
        print("Appending keyword to list...")
        keyword_list.append(keywords_df['Keyword'][x])

    return keyword_list



def keyword_scan(dataset, keyword_list):
    #for every cell(word) in dataset
    ratingcount = 0

    for word in dataset
    #see if word is in keyword list
    if keyword_list.contains(word):
        ratingcount = ratingcount + 1
        #if word is in keyword list:
        # add to ratings count for dataset and then break/pass
    #   #end if
    # 
    #after for loop, return keyword rating - 
    #which is, amount of times the word was in the keyword_list


# A test call to the keyword function.
print(keyword_list(10))
