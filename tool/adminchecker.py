from colorama import *
from urllib.request import *
from urllib.error import *
from prettytable import PrettyTable
import os
file = open('./tool/link.txt', 'r')
choice = input('InSp' + Fore.RED + '(option/AP finder)' + Fore.WHITE + '>')
myTable = PrettyTable(["Command", "Info"])
myTable.add_row(["SUrl", "link of site (www.site.com)"])
myTable.add_row(["run", " "])
#show option 1
if choice == 'show options':
	print(myTable)
	os.system('python ./tool/adminchecker.py')
#if choice is vide
elif choice == '':
	print(Fore.GREEN + '[!]' + Fore.WHITE + '[ ' + choice + ' ]' + Fore.RED + ' not found' + Fore.WHITE)
#if choice is Surl
elif choice == 'SUrl':
	url = input('InSp' + Fore.RED + '(option/AP finder/SUrl)' + Fore.WHITE + '>')
	print(Fore.RED + 'SUrl ==> ' + Fore.GREEN + url + Fore.WHITE)
	run = input('InSp' + Fore.RED + '(option/AP finder/SUrl)' + Fore.WHITE + '>')
#sub Surl if you choice is run(run methode)
	if run == 'run':
		print('[' + Fore.BLUE + '*' + Fore.WHITE + ']' + 'starting...')
		while True:
			link = file.readline().split('\n') [0]
			if not link:
				break
			req_link = 'http://' + url + '/' + link
			try:
				reponse = urlopen(req_link)
			except HTTPError as e:
				print(Fore.RED + '[-] No ==>', req_link)
				continue
			except URLError as e:
				print('[*] Url not found')
				break
				continue
			else:
				print(Fore.GREEN + '[+] Ok ==>', req_link)
#sub Surl show option 2: indicate your url (run methode)
	elif run == 'show options':
		myTable1 = PrettyTable(["Command", "Info"])
		myTable1.add_row(["SUrl", url])
		myTable1.add_row(["run", " "])
		print(myTable1)
		print('[' + Fore.BLUE + '*' + Fore.WHITE + ']' + 'starting...')
		while True:
			link = file.readline().split('\n') [0]
			if not link:
				break
			req_link = 'http://' + url + '/' + link
			try:
				reponse = urlopen(req_link)
			except HTTPError as e:
				print(Fore.RED + '[-] No ==>', req_link)
				continue
			except URLError as e:
				print('[*] Url not found')
				break
				continue
			else:
				print(Fore.GREEN + '[+] Ok ==>', req_link)
#sub Surl if you choice is vide
	elif run == '':
		os.system('clear')
		os.system('python ./tool/adminchecker.py')
#if you choice is not correct
	else:
		print(Fore.GREEN + '[!]' + Fore.WHITE + '[ ' + run + ' ]' + Fore.RED + ' not found' + Fore.WHITE)
		os.system('clear')
		os.system('python ./tool/adminchecker.py')
#if you choice is not correct
else:
	print(Fore.GREEN + '[!]' + Fore.WHITE + '[ ' + choice + ' ]' + Fore.RED + ' not found' + Fore.WHITE)
	os.system('clear')
	os.system('python ./tool/adminchecker.py')
	