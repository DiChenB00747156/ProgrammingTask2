with open(Crime, 'r') as myfile
crime_type = ["ASSAULT","ROBBERY","THEFT OF VEHICLE","BREAK AND ENTER","THEFT FROM VEHICLE"]
crimecount = 0
type_id = {}#a dict that mapping from crime types to id
id_count={}#a dict that mapping from id to count

def get_type_id(file):
	for line in myfile:
		wordlist = line.strip()
		wordlist1 = wordlist.split(',')
		for work in wordlist1:
			if word in crime_type:
				type_id[word] = 1 + type_id.get(word,0)
	return type_id

def get_id_count(file):
	for value in type_id.values():
		id_count[value] = 1 + id_count.get(value,0)
	return id_count

def print_format(dict1,dict2):
	for key in dict1:
		a = dict1[k]
		print(key,dict[key],dict2[a])
		
dict1=get_type_id(myfile)
dict2=get_id_count(myfile)
print_format(dict1,dict2

	

