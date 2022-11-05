from cisco_psswd_hasher import pwd_check, InvalidPassword, type5, type7, type8, type9
from sys import exit

def pwd_input(pwd: str):
    while True:
        try:
            pwd_check(pwd)
            return pwd
        except InvalidPassword as exception_string:
            print(f'{exception_string} Please try again or press CTRL + C to exit: ')
        except KeyboardInterrupt:
            exit()

def cisco_pwd(pwd_type: int, pwd: str):
    if pwd_type == 5:
        cleartext_password = pwd_input(pwd)
        passwd_hash = type5(cleartext_password)
        return passwd_hash
    elif pwd_type == 7:
        cleartext_password = pwd_input(pwd)
        passwd_hash = type7(cleartext_password)
        return passwd_hash
    elif pwd_type == 8:
        cleartext_password = pwd_input(pwd)
        passwd_hash = type8(cleartext_password)
        return passwd_hash
    elif pwd_type == 9:
        cleartext_password = pwd_input(pwd)
        passwd_hash = type9(cleartext_password)
        return passwd_hash
    else:
        print('\n' + 'Invalid option. Please enter 5, 7, 8 or 9 or press CTRL + C to exit: ' + '\n')
        exit()