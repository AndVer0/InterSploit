from colorama import *
import socket
import threading
import concurrent.futures
from prettytable import *
import time
import sys
print_lock = threading.Lock()
choice = input('InSp' + Fore.RED + '(option/portscanner)' + Fore.WHITE + '>')
myTable = PrettyTable(["Command", "Info"])
myTable.add_row(["SIp", "internal ip (ex: 192.168.1.1)"])
myTable.add_row(["run", " "])

if choice  == 'show options':
	print(myTable)
	
elif choice == 'SIp':
	ip = input('InSp' + Fore.RED + '(option/portscanner/SIp)' + Fore.WHITE + '>')
	print(Fore.RED + 'SIp ==> ' + Fore.GREEN + ip + Fore.WHITE)
	run = input('InSp' + Fore.RED + '(option/portscanner/SIp)' + Fore.WHITE + '>')
#sub Surl if you choice is run(run methode)
	if run == 'run':
		print('[' + Fore.BLUE + '*' + Fore.WHITE + ']' + 'starting...')
		def scan(ip, port):
			scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			scanner.settimeout(1)
			try:
				scanner.connect((ip, port))
				scanner.close()
				with print_lock:
					print(Fore.WHITE + f"[{port}]" + Fore.GREEN + " opened" + Fore.WHITE)
			except:
				print(Fore.WHITE + f"[{port}]" + Fore.RED + " not opened" + Fore.WHITE)
				pass
		with concurrent.futures.ThreadPoolExecutor(max_workers = 100) as exceutor:
			for port in range(1000):
				exceutor.submit(scan, ip, port + 1)
		print('--------------------------------')
		def scan(ip, port):
			scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			scanner.settimeout(1)
			try:
				scanner.connect((ip, port))
				scanner.close()
				with print_lock:
					print(Fore.WHITE + f"[{port}]" + Fore.GREEN + " opened" + Fore.WHITE)
			except:
				pass
		with concurrent.futures.ThreadPoolExecutor(max_workers = 100) as exceutor:
			for port in range(1000):
				exceutor.submit(scan, ip, port + 1)
#run
	elif run == 'show options':
		myTable1 = PrettyTable(["Command", "Info"])
		myTable1.add_row(["SIp", ip])
		myTable1.add_row(["run", " "])
		print(myTable1)
		print('[' + Fore.BLUE + '*' + Fore.WHITE + ']' + 'starting...')
		def scan(ip, port):
			scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			scanner.settimeout(1)
			try:
				scanner.connect((ip, port))
				scanner.close()
				with print_lock:
					print(Fore.WHITE + f"[{port}]" + Fore.GREEN + " opened" + Fore.WHITE)
			except:
				print(Fore.WHITE + f"[{port}]" + Fore.RED + " not opened" + Fore.WHITE)
				pass
		with concurrent.futures.ThreadPoolExecutor(max_workers = 100) as exceutor:
			for port in range(1000):
				exceutor.submit(scan, ip, port + 1)
		print('--------------------------------')
		def scan(ip, port):
			scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			scanner.settimeout(1)
			try:
				scanner.connect((ip, port))
				scanner.close()
				with print_lock:
					print(Fore.WHITE + f"[{port}]" + Fore.GREEN + " opened" + Fore.WHITE)
			except:
				pass
		with concurrent.futures.ThreadPoolExecutor(max_workers = 100) as exceutor:
			for port in range(1000):
				exceutor.submit(scan, ip, port + 1)
#run	
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
	