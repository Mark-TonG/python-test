pizza=[]
pizza.append('牛肉比萨')
pizza.append('榴莲比萨')
pizza.append('芝士比萨')

for p in pizza:
	print(p)

for p in pizza:
	print('我喜欢'+p+'！')

print('我真的很喜欢吃比萨！')

print('The first three items in the list are'+str(pizza[:3]))

print('The items from the middle of the list are'+str(pizza[0:3]))

print('The last three items in the list are'+str(pizza[-3:]))
