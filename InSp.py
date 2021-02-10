import pyfiglet
import os
from colorama import *
ascii_banner = pyfiglet.figlet_format("InterSploit")
print(ascii_banner + '                                                 ' + Fore.LIGHTCYAN_EX + 'v 2.1.4' + Fore.WHITE)
print('use ' + Fore.RED + 'show options ' + Fore.WHITE + 'to show options')
print('use ' + Fore.RED + 'use option/ ' + Fore.WHITE + 'to use option')
show = input('InSp>')
if show == "show options":
	print('   option/AP finder')
	print('   option/webscarper')
	print('   option/portscanner')
	print('   option/AR finder')
	print('   option/SD detector')
	print('   option/XSS scanner')
else:
	print(show + Fore.RED +' not found' + Fore.WHITE)
	print(Fore.GREEN + '[*]' + Fore.WHITE + 'use ' + Fore.RED + 'show options' + Fore.WHITE)
	print(Fore.GREEN + '[*]' + Fore.WHITE + 'use ' + Fore.RED + 'use option/' + Fore.WHITE)
	quit()
choice = input('InSp' + Fore.RED + '(choice number)' + Fore.WHITE + '>')

if choice == 'use option/AP finder':
	os.system('python ./tool/adminchecker.py')
elif choice == 'use option/webscarper':
	os.system('python ./tool/webviewer.py')
elif choice == 'use option/portscanner':
	os.system('python ./tool/portscanner.py')
elif choice == 'use option/AR finder':
	os.system('python ./tool/adminrouter.py')
elif choice == 'use option/SD detector':
	os.system('python ./tool/sdd.py')
elif choice == 'use option/XSS scanner':
	os.system('python ./tool/xss.py')
else:
	print(Fore.RED + 'Error number' + Fore.WHITE)
	print(Fore.GREEN + '[!]' + Fore.WHITE + '[ ' + choice + ' ]' + Fore.RED + ' not found' + Fore.WHITE)
	quit()
	

	
	
	
	
	
	
	
	
	
	
	
	
	

