direct = '://'

url = 'https://ldce.ac.in'

linksw = open('all_links.txt','w')
links = []

with open('hyperlinks.txt','r') as f:
	for i in f:
		if direct in i:
			links.append(i)
		else:
			link = url + i
			links.append(link)
			
unique_links = set(links)
for l in unique_links:
	if not l.endswith('pdf\n' or 'jpeg\n' or 'jpg\n' or 'doc\n'):
		linksw.write(l)

	
