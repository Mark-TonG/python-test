favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

name_list = ['Sarah', 'jack', 'Phil']

current_names = []
for name in favorite_languages.keys():
	current_names.append(name.lower())

for name in name_list:
	if name in current_names:
		print(name.title()+'，谢谢您参与了调查。')
	else:
		print(name.title()+'，我们邀请您参与一份调查。')
