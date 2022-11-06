from cisco_pwd_hash import cisco_pwd
from colorama import Fore
from time import sleep
class ConfigSwitch:
from re import match

class ConfigSwitch():

    def __init__(self, InfosSwitch: list, InfosVlan: list) -> None:
        self.infos_switch = InfosSwitch
        self.vlan_id_list = InfosVlan

    def iptest(ip, masque):
        ipd = ip.split(".")
        mad = masque.split(".")
        ipd, mad = [int(d) for d in ipd], [int(d) for d in mad]
        for d in ipd:
            if d > 256:
                return False
            if d < 0:
                return False
        if all([d == 0 for d in ipd]) or all([d == 255 for d in ipd]):
            return False
        if all([d == 0 for d in mad]) or all([d == 255 for d in mad]):
            return False
        return True

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

    def create_vlan(self, vlan_infos: str) -> str:
        entry = vlan_infos.split(':')
        if len(entry) != 4: return
        vlan_id, vlan_name, vlan_ip, vlan_mask = tuple(entry)
        if not self.iptest(vlan_ip): return
        vlan_id = int(vlan_id)
        vlan_config_line = f"interface Vlan{vlan_id}\n name {vlan_name}\n ip address {vlan_ip} {vlan_mask}"

        self.infos_switch.append(vlan_config_line)
        self.vlan_id_list.append(vlan_id)
        return vlan_config_line

    def switchport(vlans_int: list[str]) -> str:
        # vlans_int = vlans_int.split(',')
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
                switchport_line = f" switchport mode trunk\n switchport trunk allowed vlan {vlan}"
                switchport_line_all.append(switchport_line)

            else:pass

        return switchport_line_all

    def configure_interface(self) -> str:
        print("\nDo you want to configure :\n[1] FastEthernet interfaces\n[2] GigabitEthernet interfaces\n")
        interface_type = str(input("\nYour selection : "))

        if interface_type == '1':
            print("\nEnter the numeros of the interfaces you want to configure " + Fore.YELLOW + "(1 2 3 X): " + Fore.RESET)
            interface_choice = str(input("\nYour selection : "))
            interfaces_to_configure = interface_choice.split()

            for interface in interfaces_to_configure:
                print("\nWhat do you want to add on the interface " + Fore.YELLOW +  f"Fa0/{interface} ?" + Fore.RESET)
                print("[1] Add vlan(s) on interface with switchport\n")
                choice = int(input("\nYour selection : "))

                if choice == 1:
                    print("Enter the numero of vlan to configure on this port " + Fore.YELLOW + f"{self.vlan_id_list} : " + Fore.RESET)
                    vlans = str(input("\nYour selection : "))
                    vlans = vlans.split(',')
                    vlans_int = [int(vlans_int) for vlans_int in vlans]

                    check = any(item in vlans_int for item in self.vlan_id_list)
                    if check:
                        switchport_line_all = ConfigSwitch.switchport(vlans_int)
                        for switchport_line in switchport_line_all:
                            interface_config_line = f"interface Fa0/{interface}\n" + switchport_line
                            self.infos_switch.append(interface_config_line)
                    else:
                        print(Fore.RED + "\nVlans aren't created, please create them before assigment" + Fore.RESET)
                        break

        return interface_config_line

    def write_configuration(self, infos_switch: list):
        with open("config.txt", "w") as f:
                for element in self.infos_switch:
                    print(Fore.GREEN + f"Adding line : {element} in config.txt ... " + Fore.RESET)
                    sleep(.5)
                    f.write("\n" + element + "\n!")