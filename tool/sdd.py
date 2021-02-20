from colorama import *
import sys, os
import requests
from prettytable import PrettyTable
choice = input('InSp' + Fore.RED + '(option/SD detector)' + Fore.WHITE + '>')
myTable = PrettyTable(["Command", "Info"])
myTable.add_row(["SUrl", "host (ex: www.example.com)"])
myTable.add_row(["run", " "])
if choice  == 'show options':
	print(myTable)
	os.system('python ./tool/sdd.py')
elif choice == 'SUrl':
	url = input('InSp' + Fore.RED + '(option/SD detector/SUrl)' + Fore.WHITE + '>')
	print(Fore.RED + 'SUrl ==> ' + Fore.GREEN + url + Fore.WHITE)
	run = input('InSp' + Fore.RED + '(option/SD detector/SUrl)' + Fore.WHITE + '>')
	if run == 'run':
		print('[' + Fore.BLUE + '*' + Fore.WHITE + ']' + 'starting...')
		f = open('./tool/names.txt', 'r')
		r = f.read()
		su = r.splitlines()
		for sub in su:
			domaine = 'http://www.' + sub + '.' + url
			try:
				req = requests.get(domaine, "html.parser")
				if req.status_code == 200:
					print(Fore.GREEN + "[+] discover subdomaine:" + domaine + Fore.WHITE)
			except requests.ConnectionError:
				print(Fore.RED + "[-] not found subdomaine:" + domaine + Fore.WHITE)
				pass
			except KeyboardInterrupt:
				sys.exit()
	elif run == 'show options':
		myTable1 = PrettyTable(["Command", "Info"])
		myTable1.add_row(["SUrl", url])
		myTable1.add_row(["run", " "])
		print(myTable1)
		print('[' + Fore.BLUE + '*' + Fore.WHITE + ']' + 'starting...')
		f = open('./tool/names.txt', 'r')
		r = f.read()
		su = r.splitlines()
		for sub in su:
			domaine = 'http://www.' + sub + '.' + url
			try:
				req = requests.get(domaine, "html.parser")
				if req.status_code == 200:
					print(Fore.GREEN + "[+] discover subdomaine:" + domaine + Fore.WHITE)
			except requests.ConnectionError:
				print(Fore.RED + "[-] not found subdomaine:" + domaine + Fore.WHITE)
				pass
			except KeyboardInterrupt:
				sys.exit()
else:
	print(Fore.RED + choice + Fore.WHITE + ' not found')
	os.system('clear')
	os.system('python ./tool/sdd.py')