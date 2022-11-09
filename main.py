from cisco_pwd_hash import cisco_pwd
from colorama import Fore
from time import sleep
from re import match

class ConfigSwitch():

    def __init__(self, InfosSwitch: list, InfosVlan: list) -> None:
        self.infos_switch = InfosSwitch
        self.vlan_id_list = InfosVlan

    def test_ip_mask(ip: str) -> bool:

        pattern = r"\b(?:(?:2(?:[0-4][0-9]|5[0-5])|[0-1]?[0-9]?[0-9])\.){3}(?:(?:2([0-4][0-9]|5[0-5])|[0-1]?[0-9]?[0-9]))\b"

        if match(pattern, ip):
            return True
        else:
            print(Fore.RED + "IP address format not good, please retry" + Fore.RESET)
            pass

    def add_hostname(self, hostname: str) -> str:
        '''
        Take in argument a hostname for the device and convert into the line to inject
        into the config file (hostname xxxx)
        '''
        hostname_line = f"hostname {hostname}"
        self.infos_switch.append(hostname_line)
        return hostname_line

    def add_enable_pwd(self, enable_pwd: str) -> str:
        '''
        Take in argument an enable password for the device and convert into the line to inject
        into the config file (enable password xxxx)
        '''
        enable_pwd_line = f"enable password {enable_pwd}"
        self.infos_switch.append(enable_pwd_line)
        return enable_pwd_line

    def add_user_pwd_line(self, user_pwd_infos: str) -> str:
        '''
        Take in argument an username, a password and a cisco password hashing type for the device and convert into the line to inject
        into the config file (username xxxx secret x)
        '''
        entry = user_pwd_infos.split(':')
        if len(entry) != 3: return
        username, pwd, pwd_type = tuple(entry)
        pwd_hash = cisco_pwd(int(pwd_type), pwd)
        user_pwd_device_line = f"username {username} secret {pwd_type} {pwd_hash}"
        self.infos_switch.append(user_pwd_device_line)
        return user_pwd_device_line

    def add_default_gateway(self, ip):
        if ConfigSwitch.test_ip_mask(ip=ip):
            default_gateway_line = f"ip default-gateway {ip}"
        self.infos_switch.append(default_gateway_line)
        return default_gateway_line
        
    def create_vlan(self, vlan_infos: str) -> str:
        '''
        Take in argument the vlan infos :id, name, ip adress and mask (2 last optionnal), and convert into the line to inject
        into the config file (interface VlanX ip address xxxx mask xxxx)
        '''
        vlan_config_line = ""
        if vlan_infos.count(':') > 1:
            vlan_id = int(vlan_infos.split(':')[0])
            vlan_name = vlan_infos.split(':')[1]
            vlan_ip = vlan_infos.split(':')[2]
            vlan_mask = vlan_infos.split(':')[3]

            if ConfigSwitch.test_ip_mask(ip=vlan_ip) and ConfigSwitch.test_ip_mask(ip=vlan_mask):
                vlan_config_line = f"interface Vlan{vlan_id}\n name {vlan_name}\n ip address {vlan_ip} {vlan_mask}"        
        else:
            vlan_id = int(vlan_infos.split(':')[0])
            vlan_name = vlan_infos.split(':')[1]
            vlan_config_line = f"interface Vlan{vlan_id}\n name {vlan_name}"

        self.infos_switch.append(vlan_config_line)
        self.vlan_id_list.append(vlan_id)
        return vlan_config_line

    def add_switchport(vlans_int: list[str]) -> str:
        switchport_line_all = []

        for vlan in vlans_int:
            switchport_mode = str(input("Enter the switchport mode " + Fore.RED + "(access, voice, trunk) " + Fore.RESET + "" + f"for the vlan {vlan} : "))

            if switchport_mode == "access":
                switchport_line = f" switchport mode access\n switchport access vlan {vlan}"
                switchport_line_all.append(switchport_line)

            elif switchport_mode == "voice":
                switchport_line = f" switchport mode access\n switchport voice vlan {vlan}"
                switchport_line_all.append(switchport_line)

            elif switchport_mode == "trunk":
                print("\nDo you want to add the dot1q encapsulation for your trunk link ?")
                encapsulation = str(input("\nYour selection [y/n] : "))
                if encapsulation == 'y':
                    switchport_line = f" switchport mode trunk\n switchport trunk encapsulation dot1q\n switchport trunk allowed vlan {vlan}"
                elif encapsulation == 'n':
                    switchport_line = f" switchport mode trunk\n switchport trunk allowed vlan {vlan}"
                else:
                    print(Fore.RED + "Bad input." + Fore.RED)
                    pass

                switchport_line_all.append(switchport_line)

            else:pass
        return switchport_line_all

    def change_duplex(mode: str) -> str:
        if mode == "full":
            change_duplex_line = "duplex full"
        elif mode == "half":
            change_duplex_line = "duplex half"
        else:
            print(Fore.RED + "Unrecognized mode, please retry" + Fore.RED)
            ConfigSwitch.configure_interface()
            
        return change_duplex_line

    def change_traffic_speed(speed: int) -> str:
        print("\nPlease choose between full duplex and half-duplex mode")
        duplex_mode = str(input("\nYour selection [full/half]: "))
        change_duplex_line = ConfigSwitch.change_duplex(duplex_mode)

        change_traffic_speed_line = f" {change_duplex_line}\n speed {speed}"
        return change_traffic_speed_line

    def configure_interface(self) -> str:
        interface_config_lines = []
        print("\nDo you want to configure :\n[1] FastEthernet interfaces\n[2] GigabitEthernet interfaces\n")
        interface_type = int(input("\nYour selection : "))

        print("\nEnter the numeros of the interfaces you want to configure " + Fore.YELLOW + "(1 2 3 X): " + Fore.RESET)
        interface_choice = str(input("\nYour selection : "))
        interfaces_to_configure = interface_choice.split()

        for interface in interfaces_to_configure:
            if interface_type == 1:
                print("\nWhat do you want to add on the interface " + Fore.YELLOW +  f"Fa0/{interface} ?" + Fore.RESET)
            elif interface_type == 2:
                print("\nWhat do you want to add on the interface " + Fore.YELLOW +  f"Gi0/{interface} ?" + Fore.RESET)
            else:
                print("Interface type not recognized, please retry")
                ConfigSwitch.configure_interface()

            print("[1] Add vlan(s) on interface with switchport\n[2] Configure interface speed (Mb/s)\n")
            choice = int(input("\nYour selection : "))

            if choice == 1:
                print("Enter the numero of vlan to configure on this port " + Fore.YELLOW + f"{self.vlan_id_list} : " + Fore.RESET)
                vlans = str(input("\nYour selection : "))
                vlans = vlans.split(',')
                vlans_int = [int(vlans_int) for vlans_int in vlans]

                check = any(item in vlans_int for item in self.vlan_id_list)
                if check:
                    switchport_line_all = ConfigSwitch.add_switchport(vlans_int)
                    for switchport_line in switchport_line_all:
                        if interface_type == '1':
                            interface_config_line = f"interface Fa0/{interface}\n" + switchport_line
                        else:
                            interface_config_line = f"interface Gi0/{interface}\n" + switchport_line

                        interface_config_line = interface_config_line + "\n no shutdown"
                        interface_config_lines.append(interface_config_line)
                        self.infos_switch.append(interface_config_line)
                else:
                    print(Fore.RED + "\nVlans aren't created, please create them before assigment" + Fore.RESET)
                    break

            elif choice == 2:
                print("\nChoose the new interface speed (10, 100 ...)")
                new_interface_speed = int(input("\nYour selection : "))
                change_traffic_speed_line = ConfigSwitch.change_traffic_speed(new_interface_speed)

                if interface_type == '1':
                    interface_config_line = f"interface Fa0/{interface}\n" + change_traffic_speed_line
                else:
                    interface_config_line = f"interface Gi0/{interface}\n" + change_traffic_speed_line

                interface_config_line = interface_config_line + "\n no shutdown"
                interface_config_lines.append(interface_config_line)
                self.infos_switch.append(interface_config_line)

            else:
                print(Fore.RED + "\nBad choice, please retry" + Fore.RESET)
                ConfigSwitch.configure_interface()

        return interface_config_lines

    def write_configuration(self, infos_switch: list):
        with open("config.txt", "w") as f:
                for element in self.infos_switch:
                    print(Fore.GREEN + f"[+] Adding line :\n{element} in config.txt ... " + Fore.RESET)
                    sleep(.3)
                    f.write("\n" + element + "\n!")