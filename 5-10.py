current_users=['Tom','Bob','Jack','Peter','Mark']
new_users=['LUCY','Tom','ANN','jaCk','MIKE']
linshi=[]

for name in current_users:
	linshi.append(name.lower())

for new_user in new_users:
	if new_user.lower() in linshi:
		print(new_user.title()+'已被使用，需要输入其他用户名')
	else:
		print(new_user.title()+'未被使用')
