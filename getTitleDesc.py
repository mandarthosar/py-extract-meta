# Importing the modules
from bs4 import BeautifulSoup
import requests

def extracttext(domain):
    url = domain
    # Converting domain to working URL
    try:
        if requests.get('http://'+url, timeout=2):
            page = requests.get('http://'+url, timeout=2).content
        else:
            page = requests.get('https://'+url, timeout=2).content
    except:
        page = '<!Doctype html><html lang="en-US"><head><title>This site has loading issue</title><meta name="description" content="This site has loading issue"/></head><body><h1>Dummy text</h1></body></html>'

    soup= BeautifulSoup(page, 'html5lib')

    if soup.find('title'):
        title = soup.title.string
        print("Title: ",title)
    else:
        title = "There is no title for this site"

    if soup.find('meta', attrs={'name':'description'}):
        desc = soup.find('meta', attrs={'name':'description'})
        print("Desc: ",desc.get('content'))
        desc = desc.get('content')
    else:
        desc = "There is no description for this site"

    # Returning the values of title and description of the page
    return title, desc
    # print(page_title)
    # print(page_desc)

# For testing the function locally
# extracttext("1point01.com")
# extracttext("http://1point01.com")