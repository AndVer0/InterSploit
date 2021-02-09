from colorama import *
from prettytable import PrettyTable
from urllib.request import *
from urllib.error import *
choice = input('InSp' + Fore.RED + '(option/AR finder)' + Fore.WHITE + '>')
myTable = PrettyTable(["Command", "Info"])
myTable.add_row(["run", " "])
if choice  == 'show options':
	print(myTable)
	quit()
elif choice == 'run':
    print('use 192.168.1.1 / 192.168.0.1 / 192.168.8.1 in browser')
else:
	print(Fore.RED + choice + Fore.WHITE + 'not found')

