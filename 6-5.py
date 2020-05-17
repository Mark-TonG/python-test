rivers={'nile':'egypt','Yangtze':'china','yenisei':'russia'}

for key,value in rivers.items():
	print('The '+key.title()+' river runs through '+value.title()+'.')

for key in rivers.keys():
	print('The '+key.title()+' river.')

for value in rivers.values():
	print(value.title())
