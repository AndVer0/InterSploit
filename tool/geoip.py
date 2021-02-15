from colorama import *
import requests
from prettytable import PrettyTable
choice = input('InSp' + Fore.RED + '(option/geoip)' + Fore.WHITE + '>')
myTable = PrettyTable(["Command", "Info"])
myTable.add_row(["SIp", "ip"])
myTable.add_row(["run", " "])
if choice  == 'show options':
	print(myTable)
	quit()
elif choice == 'SIp':
	url = input('InSp' + Fore.RED + '(option/geoip/SIp)' + Fore.WHITE + '>')
	print(Fore.RED + 'SIp ==> ' + Fore.GREEN + url + Fore.WHITE)
	run = input('InSp' + Fore.RED + '(option/geoip/SIp)' + Fore.WHITE + '>')
	if run == 'run':
		print('[' + Fore.BLUE + '*' + Fore.WHITE + ']' + 'starting...')
		res = requests.get('https://ipinfo.io/')
		data = res.json()
		print(data)
	elif run == 'show options':
		myTable1 = PrettyTable(["Command", "Info"])
		myTable1.add_row(["SIp", url])
		myTable1.add_row(["run", " "])
		print(myTable1)
		print('[' + Fore.BLUE + '*' + Fore.WHITE + ']' + 'starting...')
		res = requests.get('https://ipinfo.io/')
		data = res.json()
		print(data)
else:
	print(Fore.RED + choice + Fore.WHITE + ' not found')