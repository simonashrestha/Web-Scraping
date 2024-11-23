# This is for Find:

from bs4 import BeautifulSoup
import requests

url = "https://www.kdnuggets.com/"

# Fetch the page content
res = requests.get(url)
htmlData = res.content

# Parse the HTML
parsedData = BeautifulSoup(htmlData, "html.parser")

# Find the first h2 tag, if it exists
h2_tag = parsedData.find('h2')
if h2_tag:
    print(h2_tag.text)
else:
    print("No <h2> tag found.")

# This is for Find all:

# import requests
# from bs4 import BeautifulSoup

# url = "https://www.kdnuggets.com/"

# # Fetch the page content
# res = requests.get(url)
# htmlData = res.content

# # Parse the HTML
# parsedData = BeautifulSoup(htmlData, "html.parser")

# # Find the first h2 tag, if it exists
# h2_tag = parsedData.find_all('h2')
# if h2_tag:
#     print(h2_tag.text)
# else:
#     print("No <h2> tag found.")
 


# import requests
# from bs4 import BeautifulSoup

# url = "https://www.kdnuggets.com/"

# # Fetch the page content
# res = requests.get(url)
# htmlData = res.content

# # Parse the HTML
# parsedData = BeautifulSoup(htmlData, "html.parser")

# # Find all anchor tags
# anchors = parsedData.find_all('a')

# # Print each link
# for anchor in anchors:
#     href = anchor.get('href')
#     if href:  # Check if href attribute exists
#         print(href)
