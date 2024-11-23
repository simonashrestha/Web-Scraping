import requests
from bs4 import BeautifulSoup

# Here we parse the data we get in the website by using BeautifulSoup where can see it in a structured way
url = "https://www.kdnuggets.com/"
res = requests.get(url)
htmlData = res.content
parsedData = BeautifulSoup(htmlData, "html.parser")
print(parsedData.prettify())
