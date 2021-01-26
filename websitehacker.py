import os
import colorama
from colorama import Fore, Back, Style
colorama.init()
def clear(): os.system('clear')
print('1: admin panel finder')
print('  ')
check = input("enter number:")
if check == '1':
  import adminchecker
  clear()
else:
	print('number not found')