from sys import exit
from main import ConfigSwitch
from colorama import Fore

def banner():
    print('''
    ▛▀▀▀▀▀▀▀▜   PyCISCO
    ▌ ▋▋▋▋▋▋▐   by @0xSp3ctra & <br>
    ▌       ▐   v1.1
    █▙▁▁▁▁▁▟█
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
vlan_id_list = []
ConfigSwitch = ConfigSwitch(InfosSwitch=infos_switch, InfosVlan=vlan_id_list)

def test(line: str) -> None:
    print(
        Fore.YELLOW + f"[+] New line saved : \n{line}" + Fore.RESET if line
        else Fore.RED + "\nInvalid input." + Fore.RESET
    )

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
            if hostname:
                hostname_line = ConfigSwitch.add_hostname(hostname)
                test(hostname_line)

        elif choice == 2:
            enable_pwd = str(input("\nEnter the enable password : "))
            if enable_pwd:
                enable_pwd_line = ConfigSwitch.add_enable_pwd(enable_pwd)
                test(enable_pwd_line)

        elif choice == 3:
            user_pwd_infos = str(input("\nEnter the infos (username:password:password_type(5,7,8,9)): "))
            if user_pwd_infos:
                user_pwd_device_line = ConfigSwitch.add_user_pwd_line(user_pwd_infos)
                test(user_pwd_device_line)

        elif choice == 4:
            vlan_infos = str(input("\nEnter the vlan infos (id:name:ip_address:mask) : "))
            if vlan_infos:
                vlan_config_line = ConfigSwitch.create_vlan(vlan_infos)
                test(vlan_config_line)

        elif choice == 5:
            interface_config_line = ConfigSwitch.configure_interface()

        elif choice == 6:
            print(Fore.YELLOW + "\n[+] Writing configuration in 'config.txt' ..." + Fore.RESET)
            ConfigSwitch.write_configuration(infos_switch)
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