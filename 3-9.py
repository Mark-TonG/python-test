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

print('抱歉，只能邀请两位来共进晚餐了。')

for x in range(0,t-2):
	a=names.pop();
	print('Dear '+a+',无法您来共进晚餐了。')
for x in range(0,2):
	print('Dear '+names[x]+',我仍邀请您共进晚餐。')

print('最后总共有'+str(len(names))+'位来共进晚餐。')

for c in range(0,2):
	del names[0]

print(names)



