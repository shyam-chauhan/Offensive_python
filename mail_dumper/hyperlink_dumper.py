import requests
import re
from bs4 import BeautifulSoup

url = ["https://books.toscrape.com/"] #urls of webpages from where you want to scrap hyperlinks

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}  #Request headers masqurading with windows firefox


for req in url: #loop until last url
    print(req)  #printing website name
    
    res = requests.get(req).text  #getting text from website
    
    soup = BeautifulSoup(res, 'html.parser') #compiling beautifulsoup for scrapping
    
    a_tag = soup.find_all('a', attrs={'href': True})   # finding all a tags with href attribute and saving it in a_tag list

    for i in a_tag: #running loop until last link
        print(i['href']) #printing value of href attribute
    
    print("\n") #adding new line after one webpage

