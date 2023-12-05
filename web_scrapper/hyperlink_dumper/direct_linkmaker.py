url = 'https://' #url to be specified

linksw = open('all_links.txt','a')

with open('indirect_links.txt','r') as f:
	for i in f:
		link = url + i
		linksw.write(link)
		
