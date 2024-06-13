# To scrape and parse text from websites in Python, you can use the requests library to fetch the HTML content of the website and then use a parsing library like BeautifulSoup or lxml to extract the relevant text from the HTML. Here’s a step-by-step guide:

"""STEP-1->IMPORTING MODULES"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

"""STEP-2->Fetch the HTML content of the website using `requests`"""
url = 'https://www.nykaa.com/search/result/?q=sunscreens&root=search&searchType=Manual&sourcepage=home'; # Replace this with the URL of the website you want to scrape

headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36'}
result = requests.get(url, headers=headers)

# Check if the request was successful
if result.status_code == 200:
    html_content = result.content
else:
    print("Failed to fetch the website.")


products=[]
prices=[]
"""Step 3: Parse the HTML content using `BeautifulSoup`"""
soup = BeautifulSoup(html_content, 'html.parser')
# Find all the text elements (e.g., paragraphs, headings, etc.) you want to scrape
text_elements = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'span'])
# Extract the text from each element and concatenate them into a single string
scraped_text = ' '.join(element.get_text() for element in text_elements)
print(scraped_text)
# df = pd.DataFrame({'Product Name':products,'Price':prices})
# df.to_csv('products1.csv', index=False, encoding='utf-8')






