import unittest
from main import ConfigSwitch

infos_switch = []
vlan_id_list = []
ConfigSwitch = ConfigSwitch(InfosSwitch=infos_switch, InfosVlan=vlan_id_list)
class TestConfigSwitch(unittest.TestCase):

    def test_add_hostname(self):
        self.assertEqual(ConfigSwitch.add_hostname("nom_switch"), "hostname nom_switch")

    def test_add_en_pwd(self):
        self.assertEqual(ConfigSwitch.add_enable_pwd("enable_pwd_colin2"), "enable password enable_pwd_colin2")

    def test_add_user_pwd(self):
        user_pwd_device_line = ConfigSwitch.add_user_pwd_line("username_coco:pwd_coco:5")
        resultat1 = user_pwd_device_line[:40]

        user_pwd_device_line = ConfigSwitch.add_user_pwd_line("username_coco:pwd_coco:5")
        resultat2 = user_pwd_device_line[:40]
        
        # self.assertEqual(resultat1, "username username_coco secret 5 $1$")
        self.assertNotEqual(resultat1, resultat2)

    def test_vlan_create(self):
        self.assertEqual(ConfigSwitch.create_vlan("10:data"), "interface Vlan10\n name data")

if __name__ == '__main__':
    unittest.main()