from colorama import Fore
from sys import exit
''' Operations on linked - list
    1.Traverse
    2.append
    3.insertion
    4.remove
    5.replace
    6. searching
    7. size of link list'''
lst = ['india', 'america', 'japan']
while True:
    print('operations on Linked-List')
    print('1.Traverse\n2.append\n3.insertion\n4.remove\n5.replace\n6.searching\n7.size of link list\n8.Exit ')
    choice = input(Fore.LIGHTCYAN_EX+'Enter your choice:'+Fore.RESET)
    if choice == '1':     # Traverse
        if lst == []:
            print('Empty List.')
        else:
            print('traversing the list.')
            for i in lst:
                print(i)

    elif choice == '8':  # Exit()
        exit('program terminated...')

    elif choice == '2':  # Append
        val = input('enter element: ')
        lst.append(val)
        print(f' {val} appended successfully...')

    elif choice == '3':    # Insertion
        val = input('enter element: ')
        ins = int(input('enter index:'))
        lst.insert(ins, val)
        print(f'{val} inserted at index {ins} successfully...')

    elif choice == '4':  # Remove
        val = input('enter element: ')
        try:
            lst.remove(val)
        except ValueError:
            print(f'{val} not found in Link-list.')

    elif choice == '5':  # replace
        try:
            val1 = input('enter element to be replaced: ')
            val2 = input('new val to be inserted: ')
            ind = lst.index(val1)
            lst[ind] = val2
            print(f'{val1} is replaced by {val2} successfully')
        except ValueError:
            print('element not found to replace or element out of index.')

    elif choice == '6':   # searching
        val = input('enter element to be searched: ')
        try:
            ind = lst.index(val)
            print(f'element found at {ind+1}')
        except ValueError:
            print(f'{val} not found in Link-list')

    elif choice == '7':  # size of Link-list
        if len(lst) == 0:
            print('Empty List.')
        else:
            print(f'Size of list : {len(lst)}')