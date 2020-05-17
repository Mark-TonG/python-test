favorite_places = {
'Mary':['北京','上海','重庆'],
'Bob':['广州'],
'Tom':['厦门', '南京']
}

for people, places in favorite_places.items():
	print(people.title()+'喜欢的地方：')
	for place in places:
		print('\t'+place)
	print('\n')
