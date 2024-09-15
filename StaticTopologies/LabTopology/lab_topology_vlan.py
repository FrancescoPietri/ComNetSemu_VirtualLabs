#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink
from sys import exit  
from mininet.node import Host
from mininet.util import quietRun
from mininet.log import error

class VLANHost( Host ):
    "Host connected to VLAN interface"

    # pylint: disable=arguments-differ
    def config( self, vlan=100, **params ):
        """Configure VLANHost according to (optional) parameters:
           vlan: VLAN ID for default interface"""

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

        return r

class LabTopologyVlan(Topo):
    "LabTopologyVlan"

    def __init__(self):

        Topo.__init__(self)

        # Define switches
        s1 = self.addSwitch('s1', dpid='0000000000000001')
        s2 = self.addSwitch('s2', dpid='0000000000000002')
        s3l1 = self.addSwitch('s3l1', dpid='0000000000000003')
        s4l2 = self.addSwitch('s4l2', dpid='0000000000000004')
        s5l3 = self.addSwitch('s5l3', dpid='0000000000000005')
        s6l4 = self.addSwitch('s6l4', dpid='0000000000000006')
        s7 = self.addSwitch('s7', dpid='0000000000000007')
        s8 = self.addSwitch('s8', dpid='0000000000000008')  
        

        # Define hosts with VLANs
        h1 = self.addHost('h1',  cls=VLANHost, vlan=1)
        h2 = self.addHost('h2',  cls=VLANHost, vlan=1)
        h3 = self.addHost('h3',  cls=VLANHost, vlan=2)
        h4 = self.addHost('h4',  cls=VLANHost, vlan=2)
        h5 = self.addHost('h5',  cls=VLANHost, vlan=3)
        h6 = self.addHost('h6',  cls=VLANHost, vlan=3)
        h7 = self.addHost('h7',  cls=VLANHost, vlan=4)
        h8 = self.addHost('h8',  cls=VLANHost, vlan=4)
        h9 = self.addHost('h9',  cls=VLANHost, vlan=5)

        # Add links between hosts and switches
        self.addLink(h1, s3l1)
        self.addLink(h2, s3l1)
        self.addLink(h3, s4l2)
        self.addLink(h4, s4l2)
        self.addLink(h5, s5l3)
        self.addLink(h6, s5l3)
        self.addLink(h7, s6l4)
        self.addLink(h8, s6l4)
        self.addLink(h9, s1)
        

        # Add links between switches
        self.addLink(s1, s2)
        self.addLink(s2, s3l1)
        self.addLink(s2, s4l2)
        self.addLink(s2, s5l3)
        self.addLink(s2, s6l4)
        self.addLink(s5l3, s8)
        self.addLink(s6l4, s8)
        self.addLink(s3l1, s7)
        self.addLink(s4l2, s7)
        self.addLink(s7, s1)
        self.addLink(s8, s1)

topos = { 'labtopologyvlan': ( lambda: LabTopologyVlan() ) }