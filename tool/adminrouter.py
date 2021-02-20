from colorama import *
from prettytable import PrettyTable
from urllib.request import *
import re
import subprocess
import os
def get_eip():
	data = str(urlopen('http://checkip.dyndns.com/').read())
	return re.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(data).group(1)
def get_un():
	meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
	data = meta_data.decode('utf-8', errors ="backslashreplace")
	data = data.split('\n')
	names = []
	for i in data:
		if "All User Profile" in i :
			i = i.split(":")
			i = i[1]
			i = i[1:-1]
			names.append(i)
	for name in names:
		print(name) 

choice = input('InSp' + Fore.RED + '(option/AR finder)' + Fore.WHITE + '>')
myTable = PrettyTable(["Command", "Info"])
myTable.add_row(["run", " "])
if choice  == 'show options':
	os.system('clear')
	os.system('python ./tool/adminrouter.py')
elif choice == 'run':
	print('[' + Fore.BLUE + '*' + Fore.WHITE + ']' + 'starting...')
	print(Fore.GREEN + '[+] Your External ip: ' + Fore.WHITE + get_eip())
	print(get_un())
else:
	print(Fore.RED + choice + Fore.WHITE + ' not found')
	os.system('clear')
	os.system('python ./tool/adminrouter.py')
