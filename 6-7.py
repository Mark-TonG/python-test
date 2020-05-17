information1 = {
		'first_name':'Mike',
		'last_name':'James',
		'age':31,
		'city':'London'
		}
information2 = {
		'first_name':'Ming',
		'last_name':'Zhang',
		'age':26,
		'city':'Beijing'
		}
information3 = {
		'first_name':'Chris',
		'last_name':'Ann',
		'age':42,
		'city':'Paris'
	}
people=[information1, information2, information3]

for information in people:
	for key,value in information.items():
		print(key.title()+':'+str(value).title())
	print('\n')
