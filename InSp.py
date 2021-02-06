import pyfiglet
import os
from colorama import *
ascii_banner = pyfiglet.figlet_format("InterSploit")
print(ascii_banner + '                                                 ' + Fore.LIGHTCYAN_EX + 'v 0.1.2' + Fore.WHITE)
print('use ' + Fore.RED + 'show options ' + Fore.WHITE + 'to show options')
show = input('InSp>')
if show == "show options":
	print(Fore.LIGHTBLUE_EX + '1. admin panel finder ' + Fore.GREEN + '(bruteforcer)' + "\n" + Fore.LIGHTBLUE_EX + '2. web scarper ' + Fore.GREEN + '(extract data)' + Fore.WHITE)
	print(Fore.LIGHTBLUE_EX + '3. Port Scanner ' + Fore.GREEN + '(Fast Bruteforcer)' + Fore.WHITE)
else:
	print(show + Fore.RED +' not found' + Fore.WHITE)
	print(Fore.GREEN + '[*]' + Fore.WHITE + 'use ' + Fore.RED + 'show options' + Fore.WHITE)
	quit()
choice = input('InSp' + Fore.RED + '(choice number)' + Fore.WHITE + '>')
if choice == '1':
	os.system('python ./tool/adminchecker.py')
elif choice == '2':
	os.system('python ./tool/webviewer.py')
elif choice == '3':
	os.system('python ./tool/portscanner.py')
else:
	print(Fore.RED + 'Error number' + Fore.WHITE)
	print(Fore.GREEN + '[!]' + Fore.WHITE + '[ ' + choice + ' ]' + Fore.RED + ' not found' + Fore.WHITE)
	quit()
	

	
	
	
	
	
	
	
	
	
	
	
	
	

