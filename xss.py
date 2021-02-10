from colorama import *
import sys
import requests
from prettytable import PrettyTable
choice = input('InSp' + Fore.RED + '(option/XSS scanner)' + Fore.WHITE + '>')
myTable = PrettyTable(["Command", "Info"])
myTable.add_row(["SUrl", "host (ex: www.example.com + get_name (ex: ?item= ))"])
myTable.add_row(["run", " "])
if choice  == 'show options':
	print(myTable)
	quit()
elif choice == 'SUrl':
	url = input('InSp' + Fore.RED + '(option/XSS scanner/SUrl)' + Fore.WHITE + '>')
	print(Fore.RED + 'SUrl ==> ' + Fore.GREEN + url + Fore.WHITE)
	run = input('InSp' + Fore.RED + '(option/XSS scanner/SUrl)' + Fore.WHITE + '>')
	if run == 'run':
		print('[' + Fore.BLUE + '*' + Fore.WHITE + ']' + 'starting...')
		payload = "<script>alert('XSS');</script>"
		req = requests.get(url + payload, "html.parser").text
		if payload in req:
			print('XSS vulnerability ' + Fore.GREEN + 'found')
		else:
			print('XSS vulnerability ' + Fore.RED + 'not found')
	elif run == 'show options':
		myTable1 = PrettyTable(["Command", "Info"])
		myTable1.add_row(["SUrl", url])
		myTable1.add_row(["run", " "])
		print(myTable1)
		print('[' + Fore.BLUE + '*' + Fore.WHITE + ']' + 'starting...')
		payload = "<script>alert('XSS');</script>"
		req = requests.get(url + payload, "html.parser").text
		if payload in req:
			print('XSS vulnerability ' + Fore.GREEN + 'found')
		else:
			print('XSS vulnerability ' + Fore.RED + 'not found')
else:
	print(Fore.RED + choice + Fore.WHITE + 'not found')