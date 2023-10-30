import requests
import re

url = ["https://ldce.ac.in", "https://sbi.co.in/web/about-us"] #urls of webpages from where you want to scrap E-mails

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}  #Request headers masqurading with windows firefox

pat = re.compile("[a-zA-Z0-9-_.]+@[a-zA-Z0-9_]+[.][a-zA-Z.]+") #regex expression I have used to findout E-mails

for req in url: #loop until last url
    print(req)  #printing website name
    res = requests.get(req).text  #getting text from website
    mail = re.findall(pat,res)   # finding patterns from webpages's text

    for i in mail: #running loop until last E-mail ID
        print(i) #printing E-mail
    
    print("\n") #adding new line after one webpage

