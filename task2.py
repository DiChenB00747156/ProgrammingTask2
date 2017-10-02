with open(Crime, 'r') as myfile
crime_type = ["ASSAULT","ROBBERY","THEFT OF VEHICLE","BREAK AND ENTER","THEFT FROM VEHICLE"]
crimecount = 0
for line in myfile:
	wordlist = line.strip()
	wordlist1 = wordlist.split(',')
	for work in wordlist1:
		if word in crime_type:
			word_index = wordlist1.find(word)
			print(word,wordlist1[word_index-1]
)

	

