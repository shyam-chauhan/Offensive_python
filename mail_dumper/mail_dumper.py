import requests
import re

url = ["https://ldce.ac.in", "https://sbi.co.in/web/about-us"]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

pat = re.compile("[a-zA-Z0-9-_.]+@[a-zA-Z0-9_]+[.][a-zA-Z.]+")

count = len(url)
for req in url:
    print(req)
    res = requests.get(req).text
    mail = re.findall(pat,res)

    for i in mail:
        print(i)
    
    print("\n")

