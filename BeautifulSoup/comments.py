from bs4 import BeautifulSoup

# It is included in the HTML headings and are present inside tag and it is one of the NavigableString.
soup = BeautifulSoup("<h1><!-- This is a comment --></h1>", "html.parser")
print(soup.h1.string)
print(type(soup.h1.string))
