from bs4 import BeautifulSoup
from colorama import *
from urllib.request  import urlopen
from prettytable import PrettyTable
choice = input('InSp' + Fore.RED + '(option/webscarper)' + Fore.WHITE + '>')
myTable = PrettyTable(["Command", "Info"])
myTable.add_row(["SUrl", "link of site (www.site.com)"])
myTable.add_row(["run", " "])
if choice  == 'show options':
	print(myTable)
elif choice == 'SUrl':
	url = input('InSp' + Fore.RED + '(option/webscarper/SUrl)' + Fore.WHITE + '>')
	print(Fore.RED + 'SUrl ==> ' + Fore.GREEN + url + Fore.WHITE)
	run = input('InSp' + Fore.RED + '(option/webscarper/SUrl)' + Fore.WHITE + '>')
#sub Surl if you choice is run(run methode)
	if run == 'run':
		print('[' + Fore.BLUE + '*' + Fore.WHITE + ']' + 'starting...')
		link = 'http://' + url
		page = urlopen(link)
		a = BeautifulSoup(page)
		print(a.prettify())
#run
	elif run == 'show options':
		myTable1 = PrettyTable(["Command", "Info"])
		myTable1.add_row(["SUrl", url])
		myTable1.add_row(["run", " "])
		print(myTable1)
		print('[' + Fore.BLUE + '*' + Fore.WHITE + ']' + 'starting...')
		
		link = 'http://' + url
		page = urlopen(link)
		a = BeautifulSoup(page)
		print(a.prettify())
		
	elif run == '':
		print(myTable)
		quit()
#if you choice is not correct
	else:
		print(Fore.GREEN + '[!]' + Fore.WHITE + '[ ' + run + ' ]' + Fore.RED + ' not found' + Fore.WHITE)
		print(myTable)
		quit()
else:
	print(Fore.RED + choice + Fore.WHITE + ' not found')