Dolores = {
	'race':'caucasian',
	'sex':'female',
	'role':'rancher\'s daughter',
}

Teddy = {
	'race':'caucasian',
	'sex':'male',
	'role':'loser',
}

Maeve = {
	'race':'black',
	'sex':'female',
	'role':'Madam',
}

hosts = [Dolores, Teddy, Maeve]

# for host in hosts:
# 	print(host)

#let's make background hosts 
new_host = {
	'race':'caucasian',
	'sex':'male',
	'role':'background player',
}	

for i in range(30):
	hosts.append(new_host)

# for host in hosts[:6]:
# 	print(host)	

for host in hosts[5:10]:
	if host['sex']=='male':
		host['sex'] = 'female'


# print(hosts[3:9])
print("total number of hosts: ", len(hosts))	