from bs4 import BeautifulSoup

# This contains the text inside a tag in a string format. 
soup = BeautifulSoup("<h1> Welcome to KDnuggets! </h1>", "html.parser")
print(soup.h1.string)
print(type(soup.h1.string))