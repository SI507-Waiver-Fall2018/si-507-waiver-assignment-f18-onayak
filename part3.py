# these should be the only imports you need

import requests
from bs4 import BeautifulSoup

# write your code here
# usage should be python3 part3.py


page = requests.get('http://michigandaily.com')
contents = page.content
soup = BeautifulSoup(contents, 'html.parser')

#print(soup.prettify())

content_mostread = soup.find('div', class_='view-most-read').find('ol').findAll('a')

#print(len(content_mostread))
#print(type(content_mostread))


#Create url for getting author

for item in content_mostread:
    print("Title: "+item.text)
    page_article = requests.get('http://michigandaily.com'+item['href'])
    content_article = page_article.content
    soup_article = BeautifulSoup(content_article, 'html.parser')
    try:
        author_name = soup_article.find("div", attrs = {"class" : "byline"}).find('div').find('a').text.strip()
        print("Author: " + author_name)            
    except AttributeError:
        print("Author: " + soup_article.find("p", attrs = {"class" : "info"}).contents[0].strip())
    except:
        print("Author details not found")
 
        
            
