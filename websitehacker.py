import pyfiglet
from colorama import Fore
ascii_banner = pyfiglet.figlet_format("WebHACKER")
print(Fore.BLUE)
print(ascii_banner)
print(Fore.WHITE)
print('1: admin panel finder (bruteforcer)')
print('2: web scarper(extract data)')
print('  ')
check = input("enter number:")

if check == '1':
  import adminchecker
elif check == '2':
	import webviewer
else:
	print('number not found')
	