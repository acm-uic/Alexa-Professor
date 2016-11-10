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
		

		firstName=profName.split(' ')[0]
		lastName=profName.split(' ')[1]
		lastName=lastName[:-1]
		#print firstName + ' ' + lastName
		queryString="https://www.ratemyprofessors.com/search.jsp?query="


		profRole=temp_soup.find(class_="main-excerpt")
		Headings=temp_soup.find_all("p")
		queryString+=firstName
		queryString=queryString+'+'
		queryString+=lastName
	#	print extract(Headings[0].string)	
		#print queryString		
		                
                rmpurl=urllib2.urlopen(queryString)
                rmpsoup=BeautifulSoup(rmpurl)

		result=rmpsoup.find_all(class_="listing PROFESSOR")
		for i in result:
			searchResult=i.find(class_="sub").string
#			print searchResult
			uic="UNIVERSITY OF ILLINOIS AT CHICAGO"
			if uic.lower()in searchResult.lower():
				print i.find(class_="main").string
#				print i.a["href"]	
				profURL="https://www.ratemyprofessors.com/"+i.a["href"]
				profRMP=urllib2.urlopen(profURL)
				profSOUP=BeautifulSoup(profRMP)
				try:
					print profSOUP.find_all(class_="grade")[0].string
                                	print extract(profSOUP.find_all(class_="grade")[2].string)

				except IndexError:
					print "error"
				#print profSOUP.find_all(class_="grade")[0].string
		#		print extract(profSOUP.find_all(class_="grade")[2].string)
	
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
	print "\n\n\n"
