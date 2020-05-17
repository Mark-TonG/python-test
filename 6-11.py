cities = {
'北京':{'country':'中国','population':'一千万','fact':'a'},
'纽约':{'country':'美国','population':'一千万','fact':'b'},
'德里':{'country':'印度','population':'三百万','fact':'c'}
}
for city,information in cities.items():
	print(city)
	for key,value in information.items():
		print('\t'+key.title()+':'+value.title())
	print('\n')

