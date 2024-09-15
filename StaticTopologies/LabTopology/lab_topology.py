#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink

class LabTopology(Topo):
    "LabTopology"

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
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        h7 = self.addHost('h7')
        h8 = self.addHost('h8')
        h9 = self.addHost('h9')

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

topos = { 'labtopology': ( lambda: LabTopology() ) }

