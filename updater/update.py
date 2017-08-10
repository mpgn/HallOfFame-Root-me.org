import json
import re
import requests
import sys

with open('../site/users.json', 'r') as data_file:
	data = json.load(data_file)

def wrong_arg():
	print("[-] Missing or wrong argument")
	print("[-] Example: \n\tupdate.py update -> to update the json\n\tupdate.py add username realname -> to add a user to the json")
	sys.exit()

def update_users(user):
	print("[+] Starting update profil")
	r = requests.get('https://www.root-me.org/'+ user['username'] + '?inc=score')

	regex = r'<span class=" forum" >(.*)</span>'
	matches = re.search(regex, r.text)
	if matches:
		user['username_r'] = "{group}".format(group = matches.group(1))

	regex = r'<span.*?>\n(.*)<span.*?>/(.*)</span>'
	matches = re.search(regex, r.text)
	if matches:
		user['rank'] = "{group}".format(group = matches.group(1))
		total_rank = "{group}".format(group = matches.group(2))

	regex = r'<span.*?>\n(.*)&nbsp;Points'
	matches = re.search(regex, r.text)
	if matches:
		user['points'] = "{group}".format(group = matches.group(1))

	regex = r'<span.*?>\n([a-z]*)&nbsp;'
	matches = re.search(regex, r.text)
	if matches:
		user['status'] = "{group}".format(group = matches.group(1))

	regex = r'<span.*?>\n([0-9]*)/([0-9]*)'
	matches = re.search(regex, r.text)
	if matches:
		user['challenges'] = "{group}".format(group = matches.group(1))
		total_challenge = "{group}".format(group = matches.group(2))

	regex = r'<h1 itemprop="givenName"><img class=\'.*? logo_auteur .*?\' src="(.*?)"'
	matches = re.search(regex, r.text)
	if matches:
		avatar = "{group}".format(group = matches.group(1))
		user['avatar'] = "https://www.root-me.org/" + avatar

	print("[+]", user['username'], user['username_r'], user['realn'], user['avatar'], user['rank'], user['points'] ,user['challenges'], user['status'])

	# Get all data from challenge
	regex = r'<span.*?>\n([0-9]*)&nbsp;Points&nbsp;([0-9]*)/([0-9]*)'
	matches = re.finditer(regex, r.text)
	for matchNum, match in enumerate(matches):
		matchNum = matchNum + 1
		print("{group}".format(group = match.group(1)),"=>", "{group}".format(group = match.group(2)),'/', "{group}".format(group = match.group(3)))

	with open('../site/users.json', 'w') as data_file:
		json.dump(data, data_file)

	print("[+] End update profil")

def update():
	print("[+] Starting Update generic information")

	# get generic data
	global r 
	r = requests.get('https://www.root-me.org/fr/Communaute/Classement/')
	regex = r'<a href=".*?>([0-9]+)</a>'
	matches = re.search(regex, r.text)
	if matches:
		data['total_points'] = "{group}".format(group = matches.group(1))

	r = requests.get('https://www.root-me.org/Capitaine-John?inc=score')
	regex = r'<span.*?>\n([0-9]*)/([0-9]*)'
	matches = re.search(regex, r.text)
	if matches:
		data['total_challenge'] = "{group}".format(group = matches.group(2))

	print("[+] End of update generic information")
	for user in data['users']:
		update_users(user)

def add_user(username, realn):
	print("[+] Starting to add user", username)

	data['users'].append({"username": username, "username_r": "", "realn": realn, "avatar": "https://www.root-me.org/local/cache-vignettes/L48xH48/auton0-5220c.png", "rank": 0, "points": 0, "challenges": 0, "status": "newbie"})
	with open('../site/users.json', 'w') as data_file:
		json.dump(data, data_file)

	print("[+] End of add")
	# then update lasted
	update_users(data['users'][-1])

# ## STARTING POINT####
if len(sys.argv) < 2:
	wrong_arg()
else:
	if sys.argv[1] == "update":
		update()
	elif sys.argv[1] == "add" and len(sys.argv) == 4:
		add_user(sys.argv[2],sys.argv[3])
	else:
		wrong_arg()

