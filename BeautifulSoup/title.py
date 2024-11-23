from bs4 import BeautifulSoup
import requests

url= "https://www.kdnuggets.com/"

res= requests.get(url)
htmlData= res.content
parsedData=BeautifulSoup(htmlData, "html.parser")

print(parsedData.title.string)
