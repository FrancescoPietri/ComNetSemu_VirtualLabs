#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink
from TopologyTools import *

class OfficeTopology(Topo):
    "OfficeTopology"

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
        h1of1 = self.addHost('h1of1')
        h2of1 = self.addHost('h2of1')
        h1of2 = self.addHost('h1of2')
        h2of2 = self.addHost('h2of2')
        h1of3 = self.addHost('h1of3')
        h2of3 = self.addHost('h2of3')
        h1mo1 = self.addHost('h1om1')
        h1pr1 = self.addHost('h1pr1')

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

topos = { 'officeotopology': ( lambda: OfficeTopology() ) }

