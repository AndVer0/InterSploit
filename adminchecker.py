import colorama
from colorama import Fore, Back, Style
colorama.init()
from urllib.request import *
from urllib.error import *

file = open('link.txt', 'r')
link = input('Enter website name(Ex:www.site.com):')

while True:
	sub_link = file.readline().split('\n') [0]
	if not sub_link:
		break
	req_link = 'http://'+link+'/'+sub_link
	try:
		reponse = urlopen(req_link)
	except HTTPError as e:
		print(Fore.RED)
		print('[-] No ==>', req_link)
		continue
	except URLError as e:
		continue
	else:
		print(Fore.GREEN)
		print("[+] Ok ==>", req_link)
		
    	
    	