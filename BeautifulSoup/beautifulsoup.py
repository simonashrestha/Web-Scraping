from bs4 import BeautifulSoup

# BeautifulSoup takes two arguments: input HTML and a parser. When HTML doc is passed to BS, it gives output in the python objects.
soup = BeautifulSoup("<h1> Welcome to KDnuggets! </h1>", "html.parser")
print(type(soup))

