# these should be the only imports you need
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
For SI 507 Waiver, fall 2018
@author: oshinnayak, onayak @umich.edu

"""

import requests
from bs4 import BeautifulSoup

# write your code here
# usage should be python3 part3.py


page = requests.get('http://michigandaily.com')
contents = page.content
soup = BeautifulSoup(contents, 'html.parser')

content_mostread = soup.find('div', class_='view-most-read').find('ol').findAll('a')

#print(len(content_mostread))
#print(type(content_mostread))


#Create url for getting author
print("Michigan Daily -- MOST READ")
for item in content_mostread:
    print(item.text)
    page_article = requests.get('http://michigandaily.com'+item['href'])
    content_article = page_article.content
    soup_article = BeautifulSoup(content_article, 'html.parser')
    try:
        author_name = soup_article.find("div", attrs = {"class" : "byline"}).find('div').find('a').text.strip()
        print("by " + author_name)            
    except AttributeError:
        print(soup_article.find("p", attrs = {"class" : "info"}).contents[0].strip())
    except:
        print("Author details not found")
