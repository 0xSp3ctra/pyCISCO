from cisco_pwd_hash import cisco_pwd

class ConfigSwitch():

    def add_hostname(hostname: str) -> str:
        return hostname

    def add_enable_pwd(enable_pwd: str) -> str:
        enable_pwd = f"enable password {enable_pwd}"
        return enable_pwd

    def add_user_pwd_line(user_pwd_infos: str) -> str:
        username = user_pwd_infos.split(':')[0]
        pwd = user_pwd_infos.split(':')[1]
        pwd_type = int(user_pwd_infos.split(':')[2])
        pwd_hash = cisco_pwd(pwd_type, pwd)
        user_pwd_device_line = f"username {username} secret {pwd_type} {pwd_hash}"
        return user_pwd_device_line, pwd_type, pwd_hash, username

    def create_vlan(vlan_infos: str) -> str:
        vlan_id = int(vlan_infos.split(':')[0])
        vlan_name = vlan_infos.split(':')[1]
        vlan_ip = vlan_infos.split(':')[2]
        vlan_mask = vlan_infos.split(':')[3]
        vlan_config_line = f"interface Vlan{vlan_id}\n name {vlan_name}\n ip address {vlan_ip} {vlan_mask}"
        return vlan_config_line