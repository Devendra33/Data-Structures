from queue_oops import *
from colorama import Fore
from sys import exit

Q = Queue()
while True:
    print(Fore.LIGHTCYAN_EX + 'Operations on Queue.' + Fore.RESET)
    print('1.add\n2.delete\n3.search\n4.exit')
    choice = input(Fore.LIGHTCYAN_EX + 'Enter your choice: ' + Fore.RESET)
    if choice == '1':
        ele = input('Enter Element:')
        Q.add(ele)

    elif choice == '2':
        Q.delete()

    elif choice == '3':
        ele = input('Enter element to be searched.')
        Q.search(ele)

    elif choice == '4':
        exit('program terminated.')

    print(Q.show())