import urllib2



url="https://www.cs.uic.edu/faculty/"
page=urllib2.urlopen(url)


from bs4 import BeautifulSoup

def extract(name):
	temp=""
	for i in name:
		if i !='\t' and i!='\n' and i!='\r':
			temp=temp+i
	return temp		

soup = BeautifulSoup(page)

data={}


ch=65
for i in range(0,27):

	string="teacher-classic-item filter-char-"+chr(ch)
	
	professors=soup.find_all(class_=string)


	for i in professors:
		j=0
		k=0
	#	print i.a["href"]
		temp_url=i.a["href"]
		profPage=urllib2.urlopen(temp_url)
		temp_soup=BeautifulSoup(profPage)
		profName=extract(temp_soup.h1.string)
		profRole=temp_soup.find(class_="main-excerpt")
		Headings=temp_soup.find_all("p")
	#	print extract(Headings[0].string)	

	#	print extract(profRole)
		data[profName]={}
		Details=temp_soup.find_all("blockquote")
		#print Details
		data[profName]["Role"]=extract(profRole.string)
		if(extract(Headings[j].string)=="Qualifications:"):
			data[profName]["Qualifications"]=extract(Details[k].string)
			j+=1
			k+=1
		if(extract(Headings[j].string)=="Contact Information:"):
			if(k!=1):
				data[profName]["Contact"]=extract(Details[k].p.getText())
			else:
				data[profName]["Contact"]=extract(Details[k].string)
			j+=1
			k+=1
	#		print Details[k].getText()
			data[profName]["Office"]=extract(Details[k].getText())
			k+=1
		#print data
	ch+=1

for i in data:
	print i ,
	print data[i]
