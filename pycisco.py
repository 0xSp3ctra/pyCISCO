from sys import exit
from main import ConfigSwitch
from colorama import Fore
from time import sleep

def banner():
    print('''
    ░░░░░░░░░░░░░░░░ pyCISCO ░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒░░░░░░░░░░░░░░░░░░░░░░░
    ░▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒░░░░░░░░░░░░░░░░░░
    ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▒▒▓▓▓▒▒▓▒▒▒▓▒▒▒▒▓▒▒▒▒▒▒▒▒▓▓▓▒▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒░░░░░░░░░░░░░
    ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▒▒▒▒▒▒▒▓▒▒▒▓▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒░░░░░░░░
    ░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒░░
    ░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█████████████████████▓░
    ░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███████████████████████████████████████████████████████████████████████████████▓░
    ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████████████████████████████████████████████▓█████████▓█████████▓████████▓█████████▓██████▓░
    ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███▓▓▓▓▓▓████████▓▓▓▓████▓▓█████▓████████████████████████████████████▓████▓▓▓▓▓▓███▓▓▓▓▓▓▓███▓▓▓██▓░
    ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███▓▓▓▓▓▓███▓▓▓██████████▓▓▓▓▓▓███▓▓▓▓▓▓▓███▓▓▓▓▓▓▓███▓▓▓▒▓▓▓███▓▓▓▒░▓██████▒░▒██████▓▒▒▓█████▒▒▓█▓░
    ░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█████████████████▓▓▓█████▓▓▒░▓██████▓▒░▓██████▓░░███████▒░▓▓██████▒░░░██████░░░▒█████▓░░▓█████░▒▓█▓░
    ░░░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█████████████████▓▒███████▓░░░▓█████▓░░░▓█████▒░░░██████░░░▓██████▒░░░██████░░░▒█████▓░░▓█████░▒▓█▓░
    ░░░░░░░▒▓▓▓▓▓▓▓▓▓▓▓▓███▓▓▓▓▓█████████▓▒███████▓░░░▓█████▓░░░▓█████▒░░░▓██▓█▓░░░▒▒▓▓▓▓▓▒▒▒▒▒▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓░
    ░░░░░░░░░░▒▓▓▓▓▓▓▓▓▓█████████████████▓▒▓▓▓▓▓▓▓▒▒▒▓▓▓▓▓▓▓▒▒▒▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█████████████████████████████████████▓░
    ░░░░░░░░░░░░░▒▓▓▓▓▓▓███▓▓▓▓███████▓▓▓▓▓▓▓█▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███████████████████████████████▓▒▒▒▒▒▒▒░░
    ░░░░░░░░░░░░░░░░▒▒▓▓██████████████▓▓▓▓▓▓▓▓▓▓█▓███▓██▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    ░░░ by @0xSp3ctra ░▒▓▓▓▓▓█████▓▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ v1.0 ░░░░

    ''')

def show_menu():
    print("\nPlease chose actions to affect on your device :\n")
    print(Fore.LIGHTBLUE_EX + "[1] " + Fore.RESET + "Give a hostname")
    print(Fore.LIGHTBLUE_EX + "[2] " + Fore.RESET + "Create enable password")
    print(Fore.LIGHTBLUE_EX + "[3] " + Fore.RESET + "Create user and password")
    print(Fore.LIGHTBLUE_EX + "[4] " + Fore.RESET + "Create Vlans")
    print(Fore.LIGHTBLUE_EX + "[5] " + Fore.RESET + "Configure interfaces")
    print(Fore.LIGHTBLUE_EX + "[6] " + Fore.RESET + "Exit pyCISCO and write configuration file\n")

infos_switch = []
vlan_list = []

def app_start():
    show_menu()
    try: 
        choice = int(input("\nYour selection: "))
    except ValueError:
        print(Fore.RED + "\nInvalid option. Please enter 1-6 or press CTRL+C to exit: \n" + Fore.RESET)
        app_start()
    except KeyboardInterrupt:
        print(Fore.RED + "\nExiting pyCISCO ...\n" + Fore.RESET)
        exit(0)
    else:
        if choice == 1:
            hostname = str(input("\nEnter the name of your device : "))
            hostname_line = ConfigSwitch.add_hostname(hostname=hostname)
            infos_switch.append(hostname_line)
            print(Fore.YELLOW + f"[+] New line saved : {hostname_line}" + Fore.RESET)
            
        elif choice == 2:
            enable_pwd = str(input("\nEnter the enable password : "))
            enable_pwd_line = ConfigSwitch.add_enable_pwd(enable_pwd=enable_pwd)
            infos_switch.append(enable_pwd_line)
            print(Fore.YELLOW + f"[+] New line saved : {enable_pwd_line}" + Fore.RESET)

        elif choice == 3:
            user_pwd_infos = str(input("\nEnter the infos (username:password:password_type(5,7,8,9)): "))
            user_pwd_device_line = ConfigSwitch.add_user_pwd_line(user_pwd_infos=user_pwd_infos)
            infos_switch.append(user_pwd_device_line)
            print(Fore.YELLOW + f"New line saved : {user_pwd_device_line}" + Fore.RESET)

        elif choice == 4:
            vlan_infos = str(input("\nEnter the vlan infos (id:name:ip_address:mask) : "))
            vlan_config_line, vlan_id = ConfigSwitch.create_vlan(vlan_infos=vlan_infos)
            vlan_list.append(vlan_id)
            infos_switch.append(vlan_config_line)
            print(Fore.YELLOW + vlan_config_line + Fore.RESET)

        elif choice == 5:
            ConfigSwitch.configure_interface()

        elif choice == 6:
            print(Fore.YELLOW + "\n[+] Writing configuration in 'config.txt' ..." + Fore.RESET)
            with open("config.txt", "w") as f:
                for element in infos_switch:
                    print(Fore.GREEN + f"Adding line : {element} in config.txt ... " + Fore.RESET)
                    sleep(.5)
                    f.write("\n" + element + "\n!")
            print(Fore.YELLOW + "\n[+] Configuration writed" + Fore.RESET)
            exit(0)
        else:
            print(Fore.RED + "\nInvalid option. Please enter 1-6 or press CTRL + C to exit: \n" + Fore.RESET)
            app_start()

def main():
    banner()
    while True:
        app_start()
         
# Start Here
if __name__ == "__main__":
    main()

