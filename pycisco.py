from sys import exit
from main import ConfigSwitch
from colorama import Fore
def banner():
    print(Fore.RED + '''  
               ____ ___ ____   ____ ___  
  _ __  _   _ / ___|_ _/ ___| / ___/ _ \ 
 | '_ \| | | | |    | |\___ \| |  | | | |
 | |_) | |_| | |___ | | ___) | |__| |_| |
 | .__/ \__, |\____|___|____/ \____\___/ 
 |_|    |___/     

by @0xSp3ctra                        v1.0                      
    ''' + Fore.RESET)

def show_menu():
    print("\nPlease chose actions to affect on your device :\n")
    print(Fore.LIGHTBLUE_EX + "[1] " + Fore.RESET + "Give a hostname")
    print(Fore.LIGHTBLUE_EX + "[2] " + Fore.RESET + "Create enable password")
    print(Fore.LIGHTBLUE_EX + "[3] " + Fore.RESET + "Create user and password")
    print(Fore.LIGHTBLUE_EX + "[4] " + Fore.RESET + "Create Vlans")
    print(Fore.LIGHTBLUE_EX + "[5] " + Fore.RESET + "Exit pyCISCO\n")

infos_switch = []

def app_start():
    show_menu()
    try: 
        choice = int(input("\nYour selection: "))
    except ValueError:
        print(Fore.RED + "\nInvalid option. Please enter 1-5 or press CTRL+C to exit: \n" + Fore.RESET)
        app_start()
    except KeyboardInterrupt:
        print(Fore.RED + "\nExiting pyCISCO ...\n" + Fore.RESET)
        exit(0)
    else:
        if choice == 1:
            hostname = str(input("\nEnter the name of your device : "))
            hostname = ConfigSwitch.add_hostname(hostname=hostname)
            infos_switch.append(hostname)
            print(Fore.YELLOW + f"[+] Hostname created : {hostname}" + Fore.RESET)
            
        elif choice == 2:
            enable_pwd = str(input("\nEnter the enable password : "))
            enable_pwd = ConfigSwitch.add_enable_pwd(enable_pwd=enable_pwd)
            infos_switch.append(enable_pwd)
            print(Fore.YELLOW + f"[+] Enable password created : {enable_pwd}" + Fore.RESET)

        elif choice == 3:
            user_pwd_infos = str(input("\nEnter the infos (username:password:password_type(5,7,8,9)): "))
            user_pwd_device_line, pwd_type, pwd_hash, username = ConfigSwitch.add_user_pwd_line(user_pwd_infos=user_pwd_infos)
            infos_switch.append(user_pwd_device_line)
            print(Fore.YELLOW + f"User and password of type {pwd_type} created : {username}:{pwd_hash}" + Fore.RESET)


        elif choice == 4:
            vlan_infos = str(input("\nEnter the vlan infos (id:name:ip_address:mask) : "))
            vlan_config_line = ConfigSwitch.create_vlan(vlan_infos=vlan_infos)
            infos_switch.append(vlan_config_line)
            print(Fore.YELLOW + vlan_config_line + Fore.RESET)

        elif choice == 5:
            print(Fore.YELLOW + "\n[+] Writing configuration in 'config.txt' ..." + Fore.RESET)
            with open("config.txt", "w") as f:
                for element in infos_switch:
                    f.write("\n" + element + "\n!")
            print(Fore.YELLOW + "\n[+] Configuration writed" + Fore.RESET)
            exit(0)
        else:
            print(Fore.RED + "\nInvalid option. Please enter 1-5 or press CTRL + C to exit: \n" + Fore.RESET)
            app_start()

def main():
    banner()
    while True:
        app_start()
         
# Start Here
if __name__ == "__main__":
    main()