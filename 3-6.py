names=[]
names.append('A')
names.append('B')
names.append('C')

for x in range(0,len(names)):
	print('Dear '+names[x]+', can you come to my dinner?')

print(names[2]+' can\'t come to my dinner.')

names[2]='D'

for x in range(0,len(names)):
	print('Dear '+names[x]+', can you come to my dinner?')

print('现在有了一个更大的餐桌。')

names.insert(0,'E')
names.insert(2,'F')
names.append('G')

t=len(names)
for x in range(0,t):
	print('Dear '+names[x]+', can you come to my dinner?')
