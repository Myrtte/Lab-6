def encode(password):
    '''encodes password by adding 3 to each digit'''
    digits = [num for num in password]
    new_pass = []
    for num in digits:
        int(num)
        if int(num) <= 6:
            new_dig = int(num) + 3
        elif int(num) == 7:
            new_dig = 0
        elif int(num) == 8:
            new_dig = 1
        elif int(num) == 9:
            new_dig = 2
        new_pass.append(str(new_dig))
    return ''.join(new_pass)


def decode():
    #FIXME make the function lol
    pass



def main():
    while True:
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit ')
        option = int(input('Please enter an option: '))
        if option == 1:
            password = input('Please enter your password to encode: ')
            password = encode(password)
            print(f'Your password has been encoded and stored!')
        elif option == 2:
            # FIXME run decode function
            pass
        elif option == 3:
            break
        else:
            print('Error: please select a valid menu option.')


if __name__ == '__main__':
    main()
    