from bs4 import BeautifulSoup

# This extracts the tag from the whole doc and return the first found tag with the same name if there are multiple other 
soup= BeautifulSoup("<h1> Welcome to KDnuggets! </h1>", 'html.parser')
print(type(soup.h1))
