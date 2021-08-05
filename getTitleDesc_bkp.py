# importing the module
from mechanize import Browser
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import URLError

br = Browser()
br.set_handle_redirect(True)

def showtext(): 
    print("This is a test print text")

def extracttext(domain):
    
    url = domain
    try:
        working_url=urlopen("https://"+url)
    except URLError:
        working_url=urlopen("http://"+url)
    
    url = domain
    br.open(working_url)

    soup = BeautifulSoup(br.open(working_url), features="html5lib")
    for tag in soup.find_all("meta"):
        if tag.get("name", None) == "description":
            desc = tag.get("content", None)
    title = br.title()

    return title, desc
