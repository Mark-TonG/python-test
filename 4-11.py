pizza=[]
pizza.append('牛肉比萨')
pizza.append('榴莲比萨')
pizza.append('芝士比萨')

for p in pizza:
	print(p)

for p in pizza:
	print('我喜欢'+p+'！')

print('我真的很喜欢吃比萨！')

my_pizzas=pizza
friend_pizzas=pizza[:]

my_pizzas.append('水果比萨')
friend_pizzas.append('BBQ比萨')

print('My favorite pizzas are:')
for x in my_pizzas:
	print(x)

print('My friend\'s favorite pizzas are:')
for x in friend_pizzas:
	print(x)
