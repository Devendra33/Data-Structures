from stack_oops import *
from sys import exit
from colorama import Fore

S = Stack()

while True:
    print('1.push\n2.pop\n3.peep\n4.search\n5.exit:')
    choice = input(Fore.LIGHTCYAN_EX+'Enter your choice:'+Fore.RESET)
    if  choice == '5':
        exit('program terminated.')
    elif choice == '1':
        val = input('Enter the element: ')
        S.push(val)
    elif choice == '2':
        S.pop()
    elif choice == '3':
        S.peep()
    elif choice == '4':
        S.search()
    print(S.show())




