Favorite_languges = {
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
}

for name in sorted(Favorite_languges.keys()):
	print(name.title(), ", thank you for taking our poll.")

for language in set(Favorite_languges.values()): 
	#used "set" to not see duplicates 
	print(language.title())	