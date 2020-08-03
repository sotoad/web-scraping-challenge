from bs4 import BeautifulSoup
import requests
import pandas as pd
from splinter import Browser
import time

def browser():
    executable_path = {'executable_path': '/Apps/Selenium/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

def scrape():
    
    #NASA Mars News
    nasa_mars_url = 'https://mars.nasa.gov/news/'
    browser.visit(nasa_mars_url)

    #Retrieve page
    response = browser.html

    #Create BeautifulSoup, results object,
    soup = BeautifulSoup(response, 'html.parser')
    results = soup.find('div', class_='list_text')

    #Article title
    article_title = results.find('div', class_='content_title').text
    article_title

    #Article text
    p_text = results.find('div', class_='article_teaser_body').text
    p_text

    #JPL Mars Space Images - Featured Image
    jpl_mars_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_mars_url)
    response = browser.html
    soup = BeautifulSoup(response, 'html.parser')

    jpl_results = soup.find('img', class_='thumb')['src']
    featured_image_url= 'https://www.jpl.nasa.gov' + jpl_results
    featured_image_url

    #Mars Weather
    mars_weather = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(mars_weather)
    response = browser.html
    soup = BeautifulSoup(response, 'html.parser')

    tweet_results = soup.find('div', class_='css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0')
    tweet_results

    #Mars Facts

    mars_facts_url = 'https://space-facts.com/mars/'
    tables = pd.read_html(mars_facts_url)
    df_tables = pd.DataFrame(tables)
    html_table = df_tables.to_html()
    html_table

    #Mars Hemispheres
    mars_hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(mars_hemispheres_url)
    response = browser.html
    soup = BeautifulSoup(response, 'html.parser')

    hemisphere_image_urls = []

    mars_hemi_results = soup.find("div", class_ = "result-list" )
    results = mars_hemi_results.find_all("div", class_="item")

    for result in results:
        title = mars_hemi_results.find("h3").text
        links = mars_hemi_results.find("a")["href"]
        image_url = "https://astrogeology.usgs.gov/" + links    
        html = browser.html
        soup=BeautifulSoup(html, "html.parser")
        hemisphere_image_urls.append({"title": title, "img_url": image_url})

    hemisphere_image_urls

