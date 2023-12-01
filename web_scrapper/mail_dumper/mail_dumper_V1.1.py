import requests
import re
from tqdm import tqdm
import time

links = []
mails_lst = []

count = 1
mailsf = open('mails.txt','w')

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}  #Request headers masqurading with windows firefox

pat = re.compile("[a-zA-Z0-9-_.]+@[a-zA-Z0-9_]+[.][a-zA-Z.]+") #regex expression I have used to findout E-mails

with open('all_links.txt','r') as f:
	try:
		for i in f:
			links.append(i)
		
		for link in tqdm(links , desc='getting mails'):
			print(link)
			res = requests.get(link,headers=headers)
			text = res.text
			mails = re.findall(pat,text)   # finding patterns from webpages's text
			print(mails)
			#mailsf.write(link)
			count = count + 1
			if count%5 == 0 :
				print("sleeping for while")
				#time.sleep(10)
			for mail in mails:
				mails_lst.append(mail)
	except:
		print("Error occured")
	finally:		
		unique_mails = set(mails_lst)
		for mail in unique_mails:
			mailsf.write(mail)
			mailsf.write('\n')
			
		mailsf.close()

		print('extraction complete')
		print('mails saved into mails.txt file')
