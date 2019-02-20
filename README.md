# BGP Vagrant Demo

- 2 directories, each containing a Vagrantfile
  - 1 virtual router
  - 1 Ubuntu box (exabgp node)

# Exercise Tasks

## Virtual router configuration
- Modify Vagrantfile to point to the correct url to download the base box
- Change first interface of the Virtual Machine from NAT to host-only in Virtualbox

## ExaBGP Node Configuration
Create a Vagrantfile with the following characteristics:
- host ip address = 192.168.33.254/24
- pip install exabgp
- Use provided config.ini file to configure exabgp with
  - neighbor 192.168.33.2
  - local-as 65000
  - peer-as 65000
- using the ExaBGP Documentation, modify the announce-route.py file to advertise at least two routes to the virtual router


# Appendix

## Notes on Virtual Router Configuration
Create a Vagrantfile with the following characteristics:
- host ip address = 192.168.1.1/24

1) download Cisco CSR1000v iso (req. CISCO login, valid US address,
export control EULA)

2) create a VM using defaults specified at
https://github.com/cldeluna/vagrant-ios-xe

2a) bunch of manual configuration before you package the box,
documented at

https://codingpackets.com/blog/cisco-csr-vagrant-box-install/ 

TODO: there is a bug with vagrant ssh and/or the router config
we can `ssh vagrant@192.168.33.2 (-i ~/.vagrant.d/insecure_private_key)`
successfully, but not `vagrant ssh`
the script is giving us an authentication failure and seems to be
trying to ssh to `vagrant@127.0.0.1`?

3) vagrant package --base <vm_name> --output ~/.vagrant.d/boxes/<box_name>.box
vagrant box add <box_name> </path/to/box_name>
vagrant box list  # to check if it was imported correctly






