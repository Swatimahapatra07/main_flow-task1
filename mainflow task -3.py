#!/usr/bin/env python
# coding: utf-8

# In[5]:


# web scraping 
import requests
from bs4 import BeautifulSoup

# url of the web site to scrape
my_url=("https://youtu.be/J3Ux5TQ4oUc?si=_F4LtHK5SgmJzm7s")

# send a get request to the web page 
my_response=requests.get(my_url)

# cheeck if the response is successful
if my_response.status_code==200:
    # parse the html content of the page
    my_soup=BeautifulSoup(my_response.text,'html.parser')
    
    #extract all the text from the web page
    my_page_text=my_soup.get_text()
    
    # extract all the links from the web page
    my_links=[a['href']for a in my_soup.find_all('a', href=True)]
    
    # extract all the images from the page 
    my_images=[img['src']for img in my_soup.find_all('img', src=True)]
    
    # print all the extracted data
    print("All the text of the page :-")
    print(my_page_text)
    
    print("/nAll the LINKS :-")
    for link in my_links:
        print(link)
    
    print("/nAll the IMAGES :-")
    for image in my_images:
        print(image)
else:
    print("The website is private")
    print(f"failed to retrieve the web page. Status code: {my_response.status_code}")






