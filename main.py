from cisco_pwd_hash import cisco_pwd
from colorama import Fore
from time import sleep
class ConfigSwitch():

    def __init__(self, InfosSwitch: list, InfosVlan: list) -> None:
        self.infos_switch = InfosSwitch
        self.infos_vlan = InfosVlan

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
        username = user_pwd_infos.split(':')[0]
        pwd = user_pwd_infos.split(':')[1]
        pwd_type = int(user_pwd_infos.split(':')[2])
        pwd_hash = cisco_pwd(pwd_type, pwd)
        user_pwd_device_line = f"username {username} secret {pwd_type} {pwd_hash}"
        self.infos_switch.append(user_pwd_device_line)
        return user_pwd_device_line

    def create_vlan(self, vlan_infos: str) -> str:
        vlan_id = int(vlan_infos.split(':')[0])
        vlan_name = vlan_infos.split(':')[1]
        vlan_ip = vlan_infos.split(':')[2]
        vlan_mask = vlan_infos.split(':')[3]
        vlan_config_line = f"interface Vlan{vlan_id}\n name {vlan_name}\n ip address {vlan_ip} {vlan_mask}"
        self.infos_switch.append(vlan_config_line)
        return vlan_config_line, vlan_id

    def switchport(vlans_id: str) -> str:
        vlans_id = vlans_id.split(',')
        switchport_line_all = []

        for vlan in vlans_id:
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

    def configure_interface() -> str:
        interface_type = str(input("\nDo you want to configure :\n[1] FastEthernet interfaces\n[2] GigabitEthernet interfaces\n"))
        if interface_type == '1':
            interface_choice = str(input("\nEnter the numeros of the interfaces you want to configure " + Fore.RED + "(1 2 3 X): " + Fore.RESET))
            interfaces_to_configure = interface_choice.split()

            for interface in interfaces_to_configure:
                print("\nWhat do you want to add on the interface " + Fore.RED +  f"Fa0/{interface} ?" + Fore.RESET)
                choice = int(input("[1] Add vlan(s) on interface with switchport\n"))

                if choice == 1:
                    vlans = str(input("Enter the numero of vlan to configure on this port " + Fore.RED + "(10,20,X) : " + Fore.RESET))
                    ConfigSwitch.switchport(vlans)

    def write_configuration(self, infos_switch: list):
        with open("config.txt", "w") as f:
                for element in self.infos_switch:
                    print(Fore.GREEN + f"Adding line : {element} in config.txt ... " + Fore.RESET)
                    sleep(.5)
                    f.write("\n" + element + "\n!")