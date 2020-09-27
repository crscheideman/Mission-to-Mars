#!/usr/bin/env python
# coding: utf-8

# Import
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd

# Set executable path and initialize chrome browser in splinter
executable_path = {'executable_path': 'chromedriver'}
browser = Browser('chrome', **executable_path)

# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)
# optional delay for loading page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('ul.item_list li.slide')

slide_elem.find("div", class_='content_title')

# Use the parent element to find the first 'a' tag and save it as 'news_title'
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title

# use the parent element to find the paragraph text
news_p = slide_elem.find("div", class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# Visit URL
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_id('full_image')
full_image_elem.click()

# find the more info button and click that
browser.is_element_present_by_text('more info', wait_time=1)
more_info_elem = browser.links.find_by_partial_text('more info')
more_info_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# find the relative image url
img_url_rel = img_soup.select_one('figure.lede a img').get("src")
img_url_rel

# use the base URL to creat an absolute URL
img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
img_url


# ## Mars Facts

df = pd.read_html('http://space-facts.com/mars/')[0]
df.columns=['description', 'Mars']
df.set_index('description', inplace=True)
df

df.to_html()


# ## Mars Weather

# Visit the weather website
url = 'https://mars.nasa.gov/insight/weather/'
browser.visit(url)

# Parse the data
html = browser.html
weather_soup = soup(html, 'html.parser')


# Scrape the Daily Weather Report table
weather_table = weather_soup.find('table', class_='mb_table')
print(weather_table.prettify())


# # D1 Scrape High-Resolution Mars' Hemisphere Images and Titles

# ## Hemispheres

# 1. Use browser to visit the URL 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)

browser.is_element_present_by_text('1024px', wait_time=1)


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

link = browser.find_by_css("a.product-item h3")

# 3. Write code to retrieve the image urls and titles for each hemisphere.
for i in range (len(link)) :
    hemispheres = {}
    image_link = browser.find_by_tag('h3')[i]
    image_link.click()
    
    img_url_hemi = browser.links.find_by_text('Sample').first
    hemispheres['img_url'] = img_url_hemi['href']
    
    hemispheres['title'] = browser.find_by_css("h2.title").text
    
    hemisphere_image_urls.append(hemispheres)
    
    browser.back()


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls



# 5. Quit the browser
browser.quit()




