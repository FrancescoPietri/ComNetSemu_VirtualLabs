import os
import os.path as op
from inspect import stack
import networkx as nx
import sys
import black
import re
from mininet.link import TCLink
import random
import json

PATH_DATASET = 'DatasetGML/'
PATH_TOPOLOGIES = 'Topologies/'
PATH_OUTTOPOLOGIES = 'HostVLANTopologies/'

VlanConfig = {}
HostToSwitchConfig = {}

def add_vlans(nameFile):
    with open('VlanConfig.json', 'r') as vlc:
        VlanConfig = json.load(vlc)

    with open('HostConfig.json', 'r') as htc:
        HostToSwitchConfig = json.load(htc)

    with open(op.join(PATH_TOPOLOGIES, nameFile), "r") as filepy:
        contents = filepy.readlines()

    indexToWrite = 15 + int(contents[1].strip("#"))

    contents.insert(9, f"""class VLANHost( Host ):
    "Host connected to VLAN interface"

    # pylint: disable=arguments-differ
    def config( self, vlan=100, **params ):

        r = super( VLANHost, self ).config( **params )

        intf = self.defaultIntf()
        # remove IP from default, "physical" interface
        self.cmd( 'ifconfig %s inet 0' % intf )
        # create VLAN interface
        self.cmd( 'vconfig add %s %d' % ( intf, vlan ) )
        # assign the host's IP to the VLAN interface
        self.cmd( 'ifconfig %s.%d inet %s' % ( intf, vlan, params['ip'] ) )
        # update the intf name and host's intf map
        newName = '%s.%d' % ( intf, vlan )
        # update the (Mininet) interface to refer to VLAN interface name
        intf.name = newName
        # add VLAN interface to host's name to intf map
        self.nameToIntf[ newName ] = intf

        return r\n\n""")


    for host in HostToSwitchConfig:
        contents.insert(indexToWrite, f"        self.addLink({host}, {HostToSwitchConfig[host]}) \n")
    contents.insert(indexToWrite, f"\n        #adding host to switch links\n")

    for host in HostToSwitchConfig:
            if not host in VlanConfig:
                contents.insert(indexToWrite, f"        {host} = self.addHost('{host}') \n")

    for host in VlanConfig:
        contents.insert(indexToWrite, f"        {host} = self.addHost('{host}', cls=VLANHost, vlan={VlanConfig[host]['vlan']}, ip='{VlanConfig[host]['ip']}') \n")
    contents.insert(indexToWrite, f"\n        #adding hosts \n")

    with open(op.join(PATH_OUTTOPOLOGIES, nameFile), "w") as f:
        contents = "".join(contents)
        f.write(contents)

if __name__ == "__main__":
    print("Enter file name to add Vlans:")
    nameFile = input()
    add_vlans(nameFile)
