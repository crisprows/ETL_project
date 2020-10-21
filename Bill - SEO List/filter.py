from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from splinter import Browser

def init_browser():
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome",**executable_path, headless=False)

def scrape():
    browser = init_browser()

    SEO_list = []


    url = "https://app.wordstream.com/fkt/app?cid=Web_Any_FreeTool_PopKW_Banner_KeywordTool&ref=undefined"
    browser.visit(url)

    html = browser.html
    soup = bs(html, "html.parser")

    #news = soup.find("div", class_="list_text")
    #news_paragraph = news.find("div", class_="article_teaser_body").text
    #news_title = news.find("div",class_="content_title").text

    test = soup.find("div", class_="col-xs-2 cell-border-left")
    test1 = test.find("span", class_="gridKeywordClass").text

    print(test1)


scrape()

