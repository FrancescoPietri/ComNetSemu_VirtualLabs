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

class OfficeTopologyVlan(Topo):
    "OfficeTopologyVlan"

    def __init__(self):

        Topo.__init__(self)

        # Define switches
        sof1 = self.addSwitch('sof1')       # Switch office 1
        sof2 = self.addSwitch('sof2')
        sof3 = self.addSwitch('sof3')
        sbb1 = self.addSwitch('sbb1')       # Switch backbone 1
        sbb2 = self.addSwitch('sbb2')
        smo1 = self.addSwitch('smo1')       # Switch main office 1
        spr1 = self.addSwitch('spr1')       # Switch print room 1

        # Define hosts with VLANs
        h1of1 = self.addHost('h1of1', cls=VLANHost, vlan=1, ip='10.0.1.1/24')
        h2of1 = self.addHost('h2of1', cls=VLANHost, vlan=1, ip='10.0.1.2/24')
        h1of2 = self.addHost('h1of2', cls=VLANHost, vlan=2, ip='10.0.2.1/24')
        h2of2 = self.addHost('h2of2', cls=VLANHost, vlan=2, ip='10.0.2.2/24')
        h1of3 = self.addHost('h1of3', cls=VLANHost, vlan=3, ip='10.0.3.1/24')
        h2of3 = self.addHost('h2of3', cls=VLANHost, vlan=3, ip='10.0.3.2/24')
        h1mo1 = self.addHost('h1om1', cls=VLANHost, vlan=4, ip='10.0.4.1/24')
        h1pr1 = self.addHost('h1pr1', cls=VLANHost, vlan=5, ip='10.0.5.1/24')

        # Add links between hosts and switches
        self.addLink(h1of1, sof1)
        self.addLink(h2of1, sof1)
        self.addLink(h1of2, sof2)
        self.addLink(h2of2, sof2)
        self.addLink(h1of3, sof3)
        self.addLink(h2of3, sof3)
        self.addLink(h1mo1, smo1)
        self.addLink(h1pr1, spr1)

        # Add links between switches
        self.addLink(sof1, sof2)
        self.addLink(sof2, sof3)
        self.addLink(sof1, sbb1)
        self.addLink(sof2, sbb1)
        self.addLink(sof3, sbb1)
        self.addLink(sof1, spr1)
        self.addLink(sof3, smo1)
        self.addLink(smo1, sbb2)
        self.addLink(spr1, sbb2)
        self.addLink(sbb1, sbb2)

topos = { 'officetopologyvlan': ( lambda: OfficeTopologyVlan() ) }
