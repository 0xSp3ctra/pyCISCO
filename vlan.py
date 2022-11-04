def switchport(mode: str, vlan_id: int, vlan_id2=None) -> str:
    if mode == "access":
        print(f" switchport mode access\n switchport access vlan {vlan_id}")
    elif mode == "voice":
        print(f" switchport mode access\n switchport voice vlan {vlan_id}")
    elif mode == "hybrid":
        print(f" switchport mode access\n switchport access vlan {vlan_id}\nswitchport voice vlan {vlan_id2}")
    

def vlan(ip_addr: str, mask: str, vlan_id: int) -> str:
    print(f"interface Vlan{vlan_id}\n ip address {ip_addr} {mask}")

vlan(ip_addr="192.168.13.24", mask="255.255.255.0", vlan_id=160)
