# Importing the modules
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import URLError

def extracttext(domain):
    url = domain
    # Converting domain to working URL
    try:
        if urlopen("http://"+url,timeout = 2):
            text = urlopen("http://"+url,timeout = 2).read()
        else:
            text = urlopen("https://"+url,timeout = 2).read()
    except:
        text = '<!Doctype html><html lang="en-US"><head><title>This site has loading issue</title><meta name="description" content="This site has loading issue"/></head><body><h1>Dummy text</h1></body></html>'

    # Extacting page information for BeautifulSoup manipulation
    soup = BeautifulSoup(text, features="html5lib")

    # Extracting title
    if soup.find_all('title'):
        for title in soup.find_all('title'):
            page_title = title.get_text()
    else:
        page_title = "Title is not available for this site"

    # Extracting meta information
    if soup.find_all('meta'):
        metas = soup.find_all('meta')
        desc  = [ meta.attrs['content'] for meta in metas if 'name' in meta.attrs and meta.attrs['name'] == 'description' ]
        if len(desc)>0:
            page_desc = desc[0]
        else:
            page_desc = "Description is not available for this site"
    else:
        page_desc = "Description is not available for this site"

    # Returning the values of title and description of the page
    return page_title, page_desc
    # print(page_title, page_desc)

