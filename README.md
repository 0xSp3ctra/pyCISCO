<hr>
  <a href="https://github.com/0xSp3ctra/pyCISCO">
    <img src="https://www.awnmtech.com/wp-content/uploads/2019/11/Cisco-Systems-executive-departures.png" align="center" alt="pyCISCO" title="Awesome Flipper Zero">
  </a>
<hr>

<h3 align="center">
  An auto-generating configuration files tool for <a href="https://cisco.com">Cisco</a> devices.<br><br>
  <a href="#">
    <img src="https://img.shields.io/badge/py-CISCO-red" alt="pyCISCO" height=24>
    <img src="https://img.shields.io/badge/powered%20by-UVSQ-purple" alt="Powered by UVSQ students" height=24>
    <img src="https://img.shields.io/github/repo-size/0xSp3ctra/pyCISCO?color=yellow" alt="pyCISCO" height=24>
    <img src="https://img.shields.io/github/commit-activity/m/0xSp3ctra/pyCISCO" alt="pyCISCO" height=24>
    <img src="https://img.shields.io/badge/version-1.0-orange" alt="pyCISCO" height=24>
  </a>
</h3>

Welcome to pyCISCO project, a tool that can generate cisco device configuration files with input arguments.
# Clone the Repository
You should clone with 

```shell
$ git clone --recursive https://github.com/0xSp3ctra/pyCISCO.git
```

Usage :
```shell
$ python3 pycisco.py
```
Example of output in config.txt file:
```shell
S1_RA
!
enable password cocotest
!
username colin secret 9 $9$lp7fRt77t7NnA5$UoLt2/4ZxmMBftHnBciaPxU7hbN9e4VlVMYhIQr1srI
!
interface Vlan100
 name management
 ip address 192.168.1.100 255.255.255.0
!
```


Download required libs
```shell
$ sudo apt-get install build-essential libssl-dev python-dev
```

Download required modules with pip
```shell
$ pip install scrypt
$ pip install colorama
$ pip install passlib
$ pip install backports.pbkdf2
```

Or with conda
```shell
$ conda install -c conda-forge scrypt
```
