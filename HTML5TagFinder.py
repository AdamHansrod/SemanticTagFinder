import urllib2

from bs4 import BeautifulSoup

def isSemanticTag(tag):
    name = tag.name
    if name == 'header':
        return True
    elif name == 'nav':
        return True
    elif name == 'section':
        return True
    elif name == 'article':
        return True
    elif name == 'aside':
        return True
    elif name == 'figcaption':
        return True
    elif name == 'figure':
        return True
    elif name == 'footer':
        return True
    else:
        return False

req = urllib2.Request('http://uopbustimetable.appspot.com/home.action')
response = urllib2.urlopen(req)
the_page = response.read()

soup = BeautifulSoup(the_page)

#print(soup.prettify())

for tag in soup.find_all(isSemanticTag):
    print(tag.name)


