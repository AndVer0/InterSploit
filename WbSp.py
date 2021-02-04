import pyfiglet
import os
from colorama import Fore
ascii_banner = pyfiglet.figlet_format("WebSploit")
print(Fore.BLUE)
print(ascii_banner)
print(Fore.WHITE)
print('1: admin panel finder (bruteforcer)')
print('2: web scarper(extract data)')
print('  ')
check = input("enter number:")
if check == '1':
		os.system('python3 ./tool/adminchecker.py')
elif check == '2':
    	os.system('python3 ./tool/webviewer.py')
else:
	print('number not found')
	
