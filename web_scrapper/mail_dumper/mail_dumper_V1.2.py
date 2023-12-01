import requests
import re
from bs4 import BeautifulSoup
from tqdm import tqdm


url = ['departments/information-technology/faculties/'
,'/departments/applied-mechanics/faculties/'
,'/departments/plastic-technology/faculties/'
,'/departments/information-technology/faculties/'
,'/departments/chemical-engineering/faculties/'
,'/departments/computer-engineering/faculties/'
,'/departments/electronics-communication-engineering/faculties/'
,'/departments/instrumentation-control-engineering/faculties/'
,'/departments/environmental-engineering/faculties/'
,'/departments/textile-technology/faculties/'
,'/departments/rubber-technology/faculties/'
,'/departments/faculties/'
,'/departments/mechanical-engineering/faculties/'
,'/departments/civil-engineering/faculties/'
,'/departments/biomedical-engineering/faculties/'
,'/departments/general/faculties/'
,'/departments/electrical-engineering/faculties/'
,'/departments/automobile-engineering/faculties/'
] #url of webpages from where you want to scrap hyperlinks

pat = re.compile("[a-zA-Z0-9-_.]+@[a-zA-Z0-9_]+[.][a-zA-Z.]+")

links = []
faculty = 'faculty'
mails = []

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}  #Request headers masqurading with windows firefox

    
for url in tqdm(url,desc='getting mails ....'):
	res = requests.get(url,headers=headers) #getting text from website
	res = res.text
	print(url)
	soup = BeautifulSoup(res, 'html.parser') #compiling beautifulsoup for scrapping
	 
	a_tag_list = soup.find_all('a', attrs={'href': True})   # finding all a tags with href attribute and saving it in a_tag list

	for i in a_tag_list:
		a_tag = i['href']
		if faculty in a_tag:
			new_url = a_tag
			res_l = requests.get(new_url).text
			mail = re.findall(pat,res_l)
			for i in mail:
				mails.append(i)
	
mail_set = set(mails)
for i in mail_set:
	print(i,'\n')
