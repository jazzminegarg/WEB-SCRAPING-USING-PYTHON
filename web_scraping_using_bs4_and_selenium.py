"""WHAT IS WEB SCRAPING"""
#Web scraping is one of the automated processes for gathering extensive information from the World Wide Web. The information found on the websites is disorganized. In order to store this data in a more organized fashion, web scraping is a useful tool. Online services, application programming interfaces (APIs), and custom code are just some of the options for scraping websites. This article will show how to use Python to perform web scraping.

"""Is Web Scraping Legal?--->/robots.txt"""
# Talking about whether web scraping is legal or not, some websites allow web scraping and some don’t. To know whether a website allows web scraping or not, you can look at the website’s “robots.txt” file. You can find this file by appending “/robots.txt” to the URL that you want to scrape. For this example, I am scraping Flipkart website. So, to see the “robots.txt” file, the URL is www.flipkart.com/robots.txt.

#Retrieve the website's robots. ...
# Parse and analyze the contents of the file to understand the website's crawling rules.
# Check if the website has specified any "Disallow" or "Allow" rules for your user agent.
# Look for any specified crawl-rate limits or visit times that you must abide by.

"""How Do You Scrape Data From A Website?"""
# When you run the code for web scraping, a request is sent to the URL that you have mentioned. As a response to the request, the server sends the data and allows you to read the HTML or XML page. The code then, parses the HTML or XML page, finds the data and extracts it.
#
# To extract data using web scraping with python, you need to follow these basic steps:
#
# Find the URL that you want to scrape
# Inspecting the Page
# Find the data you want to extract
# Write the code
# Run the code and extract the data
# Store the data in the required format
# Now let us see how to extract data from the Flipkart website using Python.


"""LIBRARIES USED"""
# Selenium:  Selenium is a web testing library. It is used to automate browser activities.
# BeautifulSoup: Beautiful Soup is a Python package for parsing HTML and XML documents. It creates parse trees that is helpful to extract the data easily.
# Pandas: Pandas is a library used for data manipulation and analysis. It is used to extract the data and store it in the desired format.


"""PREREQUISITES"""
#Python 2.x or Python 3.x with Selenium, BeautifulSoup, pandas libraries installed
# Google-chrome browser
# Ubuntu Operating System
# Let’s get started!

"""STEP1"""
# Step 1: Find the URL that you want to scrape
# For this example, we are going scrape Flipkart website to extract the Price, Name, and Rating of Laptops. The URL for this page is https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2.

"""STEP2"""
# The data is usually nested in tags. So, we inspect the page to see, under which tag the data we want to scrape is nested. To inspect the page, just right click on the element and click on “Inspect”.

"""STEP3"""
# Step 3: Find the data you want to extract
# Let’s extract the Price, Name, and Rating which is in the “div” tag respectively.

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

"""STEP-4"""
# To configure webdriver to use Chrome browser, we have to set the path to chromedriver

driver = webdriver.Chrome()
products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver.get('https://www.nykaa.com/search/result/?q=sunscreens&root=search&searchType=Manual&sourcepage=home')


"""STEP-5"""
# Now that we have written the code to open the URL, it’s time to extract the data from the website. As mentioned earlier, the data we want to extract is nested in <div> tags. So, I will find the div tags with those respective class-names, extract the data and store the data in a variable. Refer the code below:


content = driver.page_source
soup = BeautifulSoup(content,features="html.parser")
for a in soup.findAll('div', attrs={'class':'css-1rd7vky'}):   #to find all the divs having class name as given and
    # stores them as a list
    name=a.find('div', attrs={'class':'css-xrzmfa'})
    price=a.find('span',attrs={'class':'css-111z9ua'})
    products.append(name.text)
    prices.append(price.text)


"""Step 6: Store the data in a required format"""
# After extracting the data, you might want to store it in a format. This format varies depending on your requirement. For this example, we will store the extracted data in a CSV (Comma Separated Value) format. To do this, I will add the following lines to my code:

df = pd.DataFrame({'Product Name':products,'Price':prices})
df.to_csv('products.csv', index=False, encoding='utf-8')
