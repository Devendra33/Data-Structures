'''Operation on  deque(doublelly ended queue.) uses doublelly linked list internally.
1.add element from front
2.remove element from front
3.add element from rear
4.remove element from rear
5.remove an element from deque
6.count the number of element in deque.
7. reverse the deque.
'''
from colorama import Fore
from sys import exit
from collections import deque
LD = deque()

def user_input():
    val = input('Enter element')

    while val == '':
        val = input('Re-enter element(cannot be null value.)')

    return val


while True:
    print(Fore.LIGHTCYAN_EX + 'Operations on Deque.' + Fore.RESET)
    print('1.add element from front\n2.remove element from front')
    print('3.add element from rear\n4.remove element from rear')
    print('5.remove an element from deque\n6.count the number of element in deque.')
    print('7.reverse the deque.\n8.exit')
    choice = input(Fore.LIGHTCYAN_EX + 'Enter your choice: ' + Fore.RESET)
    if choice == '8':
        exit('Program terminatec...')

    elif choice == '1':
        LD.appendleft(user_input())

    elif choice == '2':
        if len(LD) == 0:
            print('deque is empty.')
        else:
            LD.pop(0)

    elif choice == '3':
        LD.append(user_input())

    elif choice == '4':
        if len(LD) == 0:
            print('deque is empty')
        else:
            LD.pop()

    elif choice == '5':
        val = input('Enter element to be removed: ')
        try:
            LD.remove(val)
        except ValueError:
            print(f'{val} not found on deque!')

    elif choice == '6':  # count function
        print(LD.count(user_input()))

    elif choice == '7':  # reverse the deque
        LD.reverse()

    print(Fore.LIGHTCYAN_EX+'Current deque: '+Fore.RESET, end='')
    for i in LD:
        print(i, end=' ')
    print()