import requests
from bs4 import BeautifulSoup

url = 'https://ldce.ac.in' #url of webpages from where you want to scrap hyperlinks

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}  #Request headers masqurading with windows firefox

f = open('hyperlinks.txt','w') #opening file in writing mode

print(url)  #printing website name
    
res = requests.get(url).text  #getting text from website
    
soup = BeautifulSoup(res, 'html.parser') #compiling beautifulsoup for scrapping
    
a_tag_list = soup.find_all('a', attrs={'href': True})   # finding all a tags with href attribute and saving it in a_tag list

a_tag_set = set(a_tag_list) #removing duplicates

print("fetching links ..........")
print("writing in file .............")

for i in a_tag_set: #running loop until last link
    f.write(i['href']) #writing in file
    f.write('\n') #adding new line after one webpage

print("links saved in hyperlinks.txt file.")
f.close()   #closing file
